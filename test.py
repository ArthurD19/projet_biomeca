"""
Script de traitement pour le projet Master 1 DIGISPORT – Modélisation Biomécanique
Sujet : Etude cinématique en cyclisme

Ce script :
- lit des fichiers .c3d (ezc3d)
- calcule le centre articulaire de la hanche via la méthode de Harrington
- calcule centres articulaires du genou, cheville, orteil, épaule, coude, sternum
- calcule angles articulaires (3D) pour hanche, genou, cheville, épaule (côté droit)
  et leurs projections dans le plan sagittal et frontal
- calcule vitesses angulaires (dérivée temporelle)
- segmente les cycles de pédalage à partir d'un marqueur proxy (toe droite)
- calcule max, min, delta et statistiques par cycle et sur l'ensemble
- enregistre les résultats (CSV) et figures (PNG)

Usage : modifier la liste `files` en bas et exécuter.

Dépendances : ezc3d, numpy, pandas, matplotlib
"""

import ezc3d
import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt

# ----------------------------- utilitaires -----------------------------

def get_marker(points, labels, name):
    """Retourne un tableau (3, n_frames) pour le marqueur demandé."
    try:
        idx = labels.index(name)
    except ValueError:
        raise ValueError(f"Marqueur '{name}' introuvable dans le c3d. Labels disponibles: {labels}")
    return points[:3, idx, :]


def mid_point(a, b):
    return 0.5 * (a + b)


def normalize(v):
    n = np.linalg.norm(v)
    if n == 0:
        return v
    return v / n


def angle_between_vectors(v1, v2):
    """Angle (rad) entre v1 et v2 pour chaque colonne (3, N) ou vecteur 3."""
    v1 = np.asarray(v1)
    v2 = np.asarray(v2)
    if v1.ndim == 1:
        v1 = v1[:, None]
    if v2.ndim == 1:
        v2 = v2[:, None]
    dot = np.sum(v1 * v2, axis=0)
    n1 = np.linalg.norm(v1, axis=0)
    n2 = np.linalg.norm(v2, axis=0)
    cos = dot / (n1 * n2 + 1e-12)
    cos = np.clip(cos, -1.0, 1.0)
    return np.arccos(cos)


def project_onto_plane(vecs, plane_normal):
    """Projette vecteurs (3,N) sur le plan défini par plane_normal."""
    plane_normal = plane_normal / (np.linalg.norm(plane_normal) + 1e-12)
    # v_proj = v - (v.n)n
    proj = vecs - np.outer(plane_normal, np.sum(vecs * plane_normal[:, None], axis=0))
    return proj

# ------------------------- Harrington hip center ------------------------

def compute_pelvis_frame(asi_r, asi_l, csi_r, csi_l, sternum=None):
    """
    Calcule le repère pelvien approximatif (origine au centre ASI, axes : x avant, y latéral gauche, z vertical)
    Entrées: arrays (3, N)
    Retourne: origin (3,N), axes (x,y,z) chacun (3,N)
    """
    center_ASI = mid_point(asi_r, asi_l)
    center_CSI = mid_point(csi_r, csi_l)

    # x_axis: vecteur de CSI->ASI (antérieur)
    x = center_ASI - center_CSI
    # y_axis: de droite ASI vers gauche ASI
    y = asi_l - asi_r
    # z_axis: cross(x,y)
    z = np.cross(x.T, y.T).T

    # normaliser chaque frame
    N = center_ASI.shape[1]
    x_n = np.zeros_like(x)
    y_n = np.zeros_like(y)
    z_n = np.zeros_like(z)
    for i in range(N):
        xi = x[:, i]
        yi = y[:, i]
        zi = np.cross(xi, yi)
        # orthonormalisation basique Gram-Schmidt
        xi_n = normalize(xi)
        yi_proj = yi - np.dot(yi, xi_n) * xi_n
        yi_n = normalize(yi_proj)
        zi_n = np.cross(xi_n, yi_n)
        x_n[:, i] = xi_n
        y_n[:, i] = yi_n
        z_n[:, i] = zi_n

    return center_ASI, x_n, y_n, z_n


def harrington_hip_centers(asi_r, asi_l, csi_r, csi_l):
    """Calcule les centres articulaires de hanche droit/gauche selon Harrington.
    Retourne arrays (3,N) pour hip_r, hip_l
    """
    center_ASI = mid_point(asi_r, asi_l)
    center_CSI = mid_point(csi_r, csi_l)

    # w: largeur des marqueurs antérieurs du pelvis
    w = np.linalg.norm(asi_r - asi_l, axis=0)
    # d: distance entre centre(ASI) et centre(CSI)
    d = np.linalg.norm(center_ASI - center_CSI, axis=0)

    # calcul du repère pelvien (pour orienter les offsets)
    origin, x_axis, y_axis, z_axis = compute_pelvis_frame(asi_r, asi_l, csi_r, csi_l)

    # offsets scalaires
    offset_x = -0.30 * d
    offset_y = -0.35 * w
    offset_z = 0.19 * w

    N = center_ASI.shape[1]
    hip_r = np.zeros_like(center_ASI)
    hip_l = np.zeros_like(center_ASI)
    for i in range(N):
        o = origin[:, i]
        ex = x_axis[:, i]
        ey = y_axis[:, i]
        ez = z_axis[:, i]
        # apply offsets in pelvis frame
        off = offset_x[i] * ex + offset_y[i] * ey
        hip_center = o + off
        hip_r[:, i] = hip_center - offset_z[i] * ez  # droit (z -)
        hip_l[:, i] = hip_center + offset_z[i] * ez  # gauche (z +)

    return hip_r, hip_l

# ---------------------------- angles & vitesses ------------------------

def compute_joint_centers(points_dict, labels):
    """Construit un dictionnaire de centres articulaires utiles (3, N_frames).
    points_dict: dictionnaire des arrays points[:3, idx, :]
    labels: liste de labels
    Retourne dict de arrays
    """
    res = {}
    # sternum
    res['sternum'] = get_marker(points_dict['raw_points'], labels, 'pPX')

    # ASI/CSI pour hanche
    asi_r = get_marker(points_dict['raw_points'], labels, 'pRightASI')
    asi_l = get_marker(points_dict['raw_points'], labels, 'pLeftASI')
    csi_r = get_marker(points_dict['raw_points'], labels, 'pRightCSI')
    csi_l = get_marker(points_dict['raw_points'], labels, 'pLeftCSI')

    hip_r, hip_l = harrington_hip_centers(asi_r, asi_l, csi_r, csi_l)
    res['hip_r'] = hip_r
    res['hip_l'] = hip_l

    # genou: midpoint des epicondyles
    res['knee_r'] = mid_point(get_marker(points_dict['raw_points'], labels, 'pRightKneeLatEpicondyle'),
                              get_marker(points_dict['raw_points'], labels, 'pRightKneeMedEpicondyle'))
    res['knee_l'] = mid_point(get_marker(points_dict['raw_points'], labels, 'pLeftKneeLatEpicondyle'),
                              get_marker(points_dict['raw_points'], labels, 'pLeftKneeMedEpicondyle'))

    # cheville: midpoint malleoles
    res['ankle_r'] = mid_point(get_marker(points_dict['raw_points'], labels, 'pRightMedMalleolus'),
                               get_marker(points_dict['raw_points'], labels, 'pRightLatMalleolus'))
    res['ankle_l'] = mid_point(get_marker(points_dict['raw_points'], labels, 'pLeftMedMalleolus'),
                               get_marker(points_dict['raw_points'], labels, 'pLeftLatMalleolus'))

    # orteils
    res['toe_r'] = get_marker(points_dict['raw_points'], labels, 'pRightToe')
    res['toe_l'] = get_marker(points_dict['raw_points'], labels, 'pLeftToe')

    # coude: midpoint epicondyles
    res['elbow_r'] = mid_point(get_marker(points_dict['raw_points'], labels, 'pRightArmLatEpicondyle'),
                               get_marker(points_dict['raw_points'], labels, 'pRightArmMedEpicondyle'))
    res['elbow_l'] = mid_point(get_marker(points_dict['raw_points'], labels, 'pLeftArmLatEpicondyle'),
                               get_marker(get_marker(points_dict['raw_points'], labels, 'pLeftArmLatEpicondyle'), labels, 'pLeftArmMedEpicondyle'))

    # épaules
    res['shoulder_r'] = get_marker(points_dict['raw_points'], labels, 'pRightAcromion')
    res['shoulder_l'] = get_marker(points_dict['raw_points'], labels, 'pLeftAcromion')

    return res


def compute_angles_and_speeds(joints, rate):
    """Calcule angles (rad) et vitesses angulaires (rad/s) pour le côté droit.
    Angles: hip (sternum-hip-knee), knee (hip-knee-ankle), ankle (knee-ankle-toe), shoulder (sternum-shoulder-elbow)
    Retourne dict avec arrays par angle.
    """
    tstep = 1.0 / rate
    N = joints['hip_r'].shape[1]

    # vecteurs
    v_hip_prox = joints['sternum'] - joints['hip_r']  # hip -> sternum
    v_hip_dist = joints['knee_r'] - joints['hip_r']   # hip -> knee
    hip_angle = angle_between_vectors(v_hip_prox, v_hip_dist)

    v_knee_prox = joints['hip_r'] - joints['knee_r']  # knee -> hip
    v_knee_dist = joints['ankle_r'] - joints['knee_r']
    knee_angle = angle_between_vectors(v_knee_prox, v_knee_dist)

    v_ankle_prox = joints['knee_r'] - joints['ankle_r']
    v_ankle_dist = joints['toe_r'] - joints['ankle_r']
    ankle_angle = angle_between_vectors(v_ankle_prox, v_ankle_dist)

    v_sh_prox = joints['sternum'] - joints['shoulder_r']
    v_sh_dist = joints['elbow_r'] - joints['shoulder_r']
    shoulder_angle = angle_between_vectors(v_sh_prox, v_sh_dist)

    # vitesses angulaires (derivée temporelle)
    hip_speed = np.gradient(hip_angle, tstep)
    knee_speed = np.gradient(knee_angle, tstep)
    ankle_speed = np.gradient(ankle_angle, tstep)
    shoulder_speed = np.gradient(shoulder_angle, tstep)

    return {
        'hip_angle': hip_angle,
        'knee_angle': knee_angle,
        'ankle_angle': ankle_angle,
        'shoulder_angle': shoulder_angle,
        'hip_speed': hip_speed,
        'knee_speed': knee_speed,
        'ankle_speed': ankle_speed,
        'shoulder_speed': shoulder_speed
    }

# ---------------------------- cycle detection -------------------------

def detect_cycles_from_toe_x(toe_x, min_period_s, rate):
    """Détecte minima locaux (pointe) sur la coordonnée X du toe (proxy de cycle)
    Retourne indices de frames pour chaque cycle start.
    """
    # dérivée
    d = np.diff(toe_x)
    idx_min = []
    N = len(toe_x)
    min_dist = int(min_period_s * rate)
    for i in range(1, N - 1):
        if d[i - 1] < 0 and d[i] > 0:
            # local minima candidate at i
            if len(idx_min) == 0 or (i - idx_min[-1]) > min_dist:
                idx_min.append(i)
    return np.array(idx_min)


def extract_cycles(signal, cycle_starts, n_points=100):
    """Extrait chaque cycle et interpolate sur n_points pour comparaison."""
    cycles = []
    for i in range(len(cycle_starts) - 1):
        a = cycle_starts[i]
        b = cycle_starts[i + 1]
        if b - a < 5:
            continue
        seg = signal[a:b]
        # interp
        x_old = np.linspace(0, 1, len(seg))
        x_new = np.linspace(0, 1, n_points)
        cycles.append(np.interp(x_new, x_old, seg))
    return np.array(cycles)

# ------------------------------- pipeline ------------------------------

def process_c3d(path, out_dir='output'):
    os.makedirs(out_dir, exist_ok=True)
    c3d = ezc3d.c3d(path)
    points = c3d['data']['points']
    labels = [l.decode('utf8') if isinstance(l, bytes) else l for l in c3d['parameters']['POINT']['LABELS']['value']]
    rate = float(c3d['parameters']['POINT']['RATE']['value'][0])

    points_dict = {'raw_points': points}

    # construire centres articulaires
    joints = compute_joint_centers(points_dict, labels)

    angles = compute_angles_and_speeds(joints, rate)

    # détecter cycles à partir du toe droit X (ajustable)
    toe_r = joints['toe_r']
    toe_x = toe_r[0, :]
    cycle_starts = detect_cycles_from_toe_x(toe_x, min_period_s=0.4, rate=rate)

    # extraire cycles pour chaque angle
    cycles = {}
    for name in ['hip_angle', 'knee_angle', 'ankle_angle', 'shoulder_angle']:
        cycles[name] = extract_cycles(angles[name], cycle_starts, n_points=100)

    # statistiques globales
    stats = {}
    for name in ['hip_angle', 'knee_angle', 'ankle_angle', 'shoulder_angle']:
        arr = angles[name]
        stats[name] = {
            'min': float(np.min(arr)),
            'max': float(np.max(arr)),
            'delta': float(np.max(arr) - np.min(arr)),
            'mean': float(np.mean(arr)),
            'std': float(np.std(arr))
        }

    # stats cycliques (par cycle moyenne & variabilité)
    cycle_stats = {}
    for name, clist in cycles.items():
        if clist.size == 0:
            cycle_stats[name] = {'n_cycles': 0}
            continue
        mean_traj = np.mean(clist, axis=0)
        std_traj = np.std(clist, axis=0)
        cycle_stats[name] = {
            'n_cycles': clist.shape[0],
            'mean_traj': mean_traj.tolist(),
            'std_traj': std_traj.tolist(),
            'mean_of_max': float(np.mean(np.max(clist, axis=1))),
            'mean_of_min': float(np.mean(np.min(clist, axis=1))),
            'std_of_max': float(np.std(np.max(clist, axis=1)))
        }

    # sauvegarde CSV des angles et vitesses
    N = angles['hip_angle'].shape[0]
    df = pd.DataFrame({
        'frame': np.arange(1, N + 1),
        'time_s': np.arange(N) / rate,
        'hip_angle_rad': angles['hip_angle'],
        'knee_angle_rad': angles['knee_angle'],
        'ankle_angle_rad': angles['ankle_angle'],
        'shoulder_angle_rad': angles['shoulder_angle'],
        'hip_speed_rad_s': angles['hip_speed'],
        'knee_speed_rad_s': angles['knee_speed'],
        'ankle_speed_rad_s': angles['ankle_speed'],
        'shoulder_speed_rad_s': angles['shoulder_speed']
    })
    base = os.path.splitext(os.path.basename(path))[0]
    csv_out = os.path.join(out_dir, base + '_angles.csv')
    df.to_csv(csv_out, index=False)

    # sauvegarde stats
    stats_out = os.path.join(out_dir, base + '_stats.json')
    import json
    with open(stats_out, 'w') as f:
        json.dump({'global_stats': stats, 'cycle_stats': cycle_stats, 'n_cycle_starts': len(cycle_starts)}, f, indent=2)

    # plots (exemple : angles sur tout le signal)
    plt.figure(figsize=(10, 6))
    t = np.arange(N) / rate
    plt.plot(t, angles['hip_angle'], label='Hip')
    plt.plot(t, angles['knee_angle'], label='Knee')
    plt.plot(t, angles['ankle_angle'], label='Ankle')
    plt.plot(t, angles['shoulder_angle'], label='Shoulder')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Angle (rad)')
    plt.title(base + ' - angles')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, base + '_angles.png'))
    plt.close()

    # plot cycles mean + std for hip as example
    if cycles['hip_angle'].size:
        mean = cycle_stats['hip_angle']['mean_traj']
        std = cycle_stats['hip_angle']['std_traj']
        x = np.linspace(0, 100, len(mean))
        plt.figure(figsize=(6, 4))
        plt.plot(x, mean)
        plt.fill_between(x, np.array(mean) - np.array(std), np.array(mean) + np.array(std), alpha=0.3)
        plt.xlabel('% cycle')
        plt.ylabel('Angle (rad)')
        plt.title(base + ' - Hip mean cycle')
        plt.tight_layout()
        plt.savefig(os.path.join(out_dir, base + '_hip_cycle.png'))
        plt.close()

    print(f"Traitement terminé pour {base} -> {csv_out}, {stats_out}")
    return {'csv': csv_out, 'stats': stats_out, 'n_cycle_starts': len(cycle_starts)}

# ------------------------------- main ---------------------------------
if __name__ == '__main__':
    # Modifier ici la liste des fichiers à traiter
    files = [
        'data/Chrono250_c3d.c3d',
        'data/Chrono300_c3d.c3d',
        'data/Chrono350_c3d.c3d',
        'data/Route250_c3d.c3d',
        'data/Route300_c3d.c3d',
        'data/Route350_c3d.c3d'
    ]

    for f in files:
        try:
            process_c3d(f, out_dir='output')
        except Exception as e:
            print(f"Erreur en traitant {f}: {e}")

    print('Tous les traitements sont terminés.')
