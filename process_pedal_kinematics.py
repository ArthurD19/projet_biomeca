"""
process_pedal_kinematics.py

Usage:
    python process_pedal_kinematics.py

Description:
    - Reads all .c3d files from ./data
    - Estimates Hip Joint Centers using Harrington offsets
    - Filters marker trajectories
    - Detects pedal cycles using a pedal marker (automatic fallback)
    - Computes joint angles (hip, knee, ankle) for the right side
    - Builds mean +/- SD cycle for each trial
    - Saves per-trial CSVs and PNG figures in ./results
    - Exports a summary table (ROMs) summarizing all trials

Dependencies:
    pip install ezc3d numpy scipy pandas matplotlib

Notes:
    - This script tries to be robust to slight differences in marker names.
    - Inspect the printed label list if markers are not found and adapt the mapping.

"""

import os
import glob
import ezc3d
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import pandas as pd

# --------------------------- Utilities ---------------------------

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)


def butter_lowpass_filter(data, fc, fs, order=4):
    b, a = signal.butter(order, fc / (fs / 2), btype='low')
    return signal.filtfilt(b, a, data, axis=0)


def norm(v):
    return np.linalg.norm(v, axis=-1)


def angle_between_vectors(u, v):
    dot = np.sum(u * v, axis=-1)
    nu = np.linalg.norm(u, axis=-1)
    nv = np.linalg.norm(v, axis=-1)
    cos = dot / (nu * nv + 1e-12)
    cos = np.clip(cos, -1.0, 1.0)
    return np.degrees(np.arccos(cos))

# --------------------------- Marker helpers ---------------------------

def label_index_map(labels):
    # return dict label->index
    return {l: i for i, l in enumerate(labels)}


def find_label(labels, candidates):
    # candidates: list of possible names (ordered). Try exact then partial match.
    for c in candidates:
        if c in labels:
            return labels.index(c)
    # partial startswith or contains
    lowers = [l.lower() for l in labels]
    for c in candidates:
        cl = c.lower()
        for i, l in enumerate(lowers):
            if l == cl or cl in l or l in cl:
                return i
    return None

# --------------------------- Harrington HJC ---------------------------

def compute_pelvis_metrics(frames, idx_pRightASI, idx_pLeftASI, idx_pRightCSI, idx_pLeftCSI):
    pR_ASI = frames[:, idx_pRightASI, :]
    pL_ASI = frames[:, idx_pLeftASI, :]
    pR_CSI = frames[:, idx_pRightCSI, :]
    pL_CSI = frames[:, idx_pLeftCSI, :]
    center_ASI = (pR_ASI + pL_ASI) / 2.0
    center_CSI = (pR_CSI + pL_CSI) / 2.0
    # w: mean distance right-left ASI
    w = np.mean(norm(pR_ASI - pL_ASI))
    # d: mean distance between ASI center and CSI center
    d = np.mean(norm(center_ASI - center_CSI))
    pelvis_center = (center_ASI + center_CSI) / 2.0
    return pelvis_center, w, d, center_ASI, center_CSI


def harrington_HJC_per_frame(pelvis_center_frames, w, d, side='R'):
    # apply provided offsets per frame
    offx = -0.30 * d
    offy = -0.35 * w
    offz = 0.19 * w if side == 'L' else -0.19 * w
    offs = np.array([offx, offy, offz])
    # pelvis_center_frames: n_frames x 3
    return pelvis_center_frames + offs

# --------------------------- Processing single file ---------------------------

def read_markers(c3d_path):
    c3d = ezc3d.c3d(c3d_path)
    points = c3d['data']['points']  # shape (4, n_points, n_frames)
    raw_labels = c3d['parameters']['POINT']['LABELS']['value']
    labels = []
    for l in raw_labels:
        # ezc3d may return bytes or str depending on version
        if isinstance(l, bytes):
            labels.append(l.decode('utf-8'))
        else:
            labels.append(str(l))
    frames = points[:3, :, :].transpose(2, 1, 0)  # n_frames x n_points x 3
    fs = float(c3d['parameters']['POINT']['RATE']['value'][0])
    return frames, labels, fs


def detect_pedal_peaks(pedal_marker_z, fs):
    # Smooth signal slightly
    pedal_s = signal.savgol_filter(pedal_marker_z, 11 if len(pedal_marker_z) > 11 else 5, 3)
    # find peaks separated by at least 0.6s
    distance = int(0.6 * fs)
    peaks, props = signal.find_peaks(pedal_s, distance=distance)
    # if too few peaks, try inverted peaks
    if len(peaks) < 3:
        peaks, props = signal.find_peaks(-pedal_s, distance=distance)
    return peaks


def extract_cycles_from_signal(signal1d, peaks, n_points=100):
    cycles = []
    for i in range(len(peaks) - 1):
        s, e = peaks[i], peaks[i + 1]
        if e - s < 10:
            continue
        seg = signal1d[s:e + 1]
        x_old = np.linspace(0, 1, len(seg))
        x_new = np.linspace(0, 1, n_points)
        cycles.append(np.interp(x_new, x_old, seg))
    if len(cycles) == 0:
        return np.zeros((0, n_points))
    return np.vstack(cycles)


def process_file(path, results_dir='results'):
    print(f"Processing {path}")
    frames, labels, fs = read_markers(path)
    lblmap = label_index_map(labels)

    # common Xsens-ish names candidates
    candidates = {
        'pRightASI': ['pRightASI', 'RASI', 'RightASI', 'pRASI'],
        'pLeftASI': ['pLeftASI', 'LASI', 'LeftASI', 'pLASI'],
        'pRightCSI': ['pRightCSI', 'RPSI', 'RightPSI', 'pRCSI', 'RCSI'],
        'pLeftCSI': ['pLeftCSI', 'LPSI', 'LeftPSI', 'pLCSI', 'LCSI'],
        'R_KNE': ['RKN', 'RightKnee', 'rKNE', 'RightKNE', 'pRightKNE', 'Right_Knee', 'RKNE'],
        'R_ANK': ['RAN', 'RightAnkle', 'rANK', 'pRightANK', 'RANK', 'Right_Ankle'],
        'R_TOE': ['RTOE', 'RightToes', 'RightToe', 'rTOE', 'pRightTOE', 'RTOE'],
        'R_HEE': ['RHEE', 'RightHeel', 'RightHee', 'RHEEL']
    }

    # find indices
    idx = {}
    for k, cand in candidates.items():
        res = find_label(labels, cand)
        idx[k] = res
        if res is None:
            print(f"Warning: could not find marker for {k}. Tried {cand}")

    # require at least pelvis markers and one pedal marker and knee/ankle
    required = ['pRightASI', 'pLeftASI', 'pRightCSI', 'pLeftCSI']
    if any(idx[r] is None for r in required):
        raise RuntimeError(f"Missing required pelvis markers in {path}. Found labels: {labels}")

    pelvis_center_frames, w, d, center_ASI, center_CSI = compute_pelvis_metrics(
        frames, idx['pRightASI'], idx['pLeftASI'], idx['pRightCSI'], idx['pLeftCSI'])

    H_R = harrington_HJC_per_frame(pelvis_center_frames, w, d, side='R')
    H_L = harrington_HJC_per_frame(pelvis_center_frames, w, d, side='L')

    # Filter markers
    fc = 6.0
    frames_f = butter_lowpass_filter(frames, fc, fs, order=4)

    # Right side vectors
    if idx['R_KNE'] is None or idx['R_ANK'] is None:
        raise RuntimeError(f"Missing right knee/ankle markers in {path}. Labels: {labels}")

    thigh = frames_f[:, idx['R_KNE'], :] - H_R  # thigh vector from hip
    shank = frames_f[:, idx['R_ANK'], :] - frames_f[:, idx['R_KNE'], :]
    foot = frames_f[:, idx['R_TOE'], :] - frames_f[:, idx['R_ANK'], :] if idx['R_TOE'] is not None else None

    # knee angle between thigh and shank
    knee_angle = angle_between_vectors(thigh, shank)

    # hip angle: angle between vertical pelvis->shoulder proxy and thigh
    # Xsens may have trunk markers; fallback to pelvis center to ASI center as proxy
    pelvis_forward = center_ASI - pelvis_center_frames  # not perfect but usable
    # take projection to same plane as thigh if desired; here compute 3D angle
    hip_angle = angle_between_vectors(pelvis_forward, thigh)

    # ankle angle: between shank and foot
    ankle_angle = angle_between_vectors(shank, foot) if foot is not None else np.full(knee_angle.shape, np.nan)

    # Detect cycles using pedal marker (toe Z) or ankle Z
    pedal_idx = idx['R_TOE'] if idx['R_TOE'] is not None else idx['R_ANK']
    pedal_z = frames_f[:, pedal_idx, 2]
    peaks = detect_pedal_peaks(pedal_z, fs)
    if len(peaks) < 3:
        print(f"Warning: few pedal peaks found ({len(peaks)}). Trying alternate detection via x coordinate.")
        pedal_x = frames_f[:, pedal_idx, 0]
        peaks = detect_pedal_peaks(pedal_x, fs)

    cycles_knee = extract_cycles_from_signal(knee_angle, peaks, n_points=100)
    cycles_hip = extract_cycles_from_signal(hip_angle, peaks, n_points=100)
    cycles_ankle = extract_cycles_from_signal(ankle_angle, peaks, n_points=100)

    mean_knee = np.nanmean(cycles_knee, axis=0) if cycles_knee.size else np.full(100, np.nan)
    sd_knee = np.nanstd(cycles_knee, axis=0) if cycles_knee.size else np.full(100, np.nan)

    mean_hip = np.nanmean(cycles_hip, axis=0) if cycles_hip.size else np.full(100, np.nan)
    sd_hip = np.nanstd(cycles_hip, axis=0) if cycles_hip.size else np.full(100, np.nan)

    mean_ankle = np.nanmean(cycles_ankle, axis=0) if cycles_ankle.size else np.full(100, np.nan)
    sd_ankle = np.nanstd(cycles_ankle, axis=0) if cycles_ankle.size else np.full(100, np.nan)

    # Save results
    ensure_dir(results_dir)
    base = os.path.splitext(os.path.basename(path))[0]

    # save mean cycle CSV
    df_cycles = pd.DataFrame({
        'percent_cycle': np.linspace(0, 100, 100),
        'knee_mean': mean_knee, 'knee_sd': sd_knee,
        'hip_mean': mean_hip, 'hip_sd': sd_hip,
        'ankle_mean': mean_ankle, 'ankle_sd': sd_ankle
    })
    df_cycles.to_csv(os.path.join(results_dir, f'{base}_mean_cycle.csv'), index=False)

    # save figure
    x = np.linspace(0, 100, 100)
    plt.figure(figsize=(8, 6))
    plt.plot(x, mean_knee, label='Knee mean')
    plt.fill_between(x, mean_knee - sd_knee, mean_knee + sd_knee, alpha=0.25)
    plt.plot(x, mean_hip, label='Hip mean')
    plt.fill_between(x, mean_hip - sd_hip, mean_hip + sd_hip, alpha=0.15)
    if not np.all(np.isnan(mean_ankle)):
        plt.plot(x, mean_ankle, label='Ankle mean')
        plt.fill_between(x, mean_ankle - sd_ankle, mean_ankle + sd_ankle, alpha=0.1)
    plt.xlabel('% cycle')
    plt.ylabel('Angle (deg)')
    plt.title(base)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, f'{base}_mean_cycle.png'))
    plt.close()

    # compute ROMs and some summary stats
    rom_knee = np.nanmax(cycles_knee) - np.nanmin(cycles_knee) if cycles_knee.size else np.nan
    rom_hip = np.nanmax(cycles_hip) - np.nanmin(cycles_hip) if cycles_hip.size else np.nan
    rom_ankle = np.nanmax(cycles_ankle) - np.nanmin(cycles_ankle) if cycles_ankle.size else np.nan

    summary = {
        'file': base,
        'n_cycles': cycles_knee.shape[0] if cycles_knee.size else 0,
        'rom_knee_deg': float(rom_knee) if not np.isnan(rom_knee) else None,
        'rom_hip_deg': float(rom_hip) if not np.isnan(rom_hip) else None,
        'rom_ankle_deg': float(rom_ankle) if not np.isnan(rom_ankle) else None,
        'w_pelvis_mean_m': float(w),
        'd_pelvis_mean_m': float(d)
    }

    # save HJC sample (mean)
    hjc_mean = {'H_R_x': float(np.nanmean(H_R[:, 0])), 'H_R_y': float(np.nanmean(H_R[:, 1])), 'H_R_z': float(np.nanmean(H_R[:, 2]))}
    summary.update(hjc_mean)

    return summary

# --------------------------- Batch processing ---------------------------

def main(data_dir='data', results_dir='results'):
    files = sorted(glob.glob(os.path.join(data_dir, '*.c3d')))
    if len(files) == 0:
        print('No .c3d files found in', data_dir)
        return
    ensure_dir(results_dir)
    summaries = []
    for f in files:
        try:
            s = process_file(f, results_dir=results_dir)
            summaries.append(s)
        except Exception as e:
            print(f"Error processing {f}: {e}")

    if summaries:
        df = pd.DataFrame(summaries)
        df.to_csv(os.path.join(results_dir, 'summary_roms.csv'), index=False)
        print('Saved summary to', os.path.join(results_dir, 'summary_roms.csv'))
    else:
        print('No successful processing to summarize.')


if __name__ == '__main__':
    main()
