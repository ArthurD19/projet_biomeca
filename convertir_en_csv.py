import ezc3d
import csv

# Dictionnaire : nom du CSV → fichier C3D à lire
fichiers = {
    "Chrono250": "data/Chrono250_c3d.c3d",
    "Chrono300": "data/Chrono300_c3d.c3d",
    "Chrono350": "data/Chrono350_c3d.c3d",
    "Route250":  "data/Route250_c3d.c3d",
    "Route300":  "data/Route300_c3d.c3d",
    "Route350":  "data/Route350_c3d.c3d",
}

for nom, chemin in fichiers.items():

    c3d = ezc3d.c3d(chemin)
    points = c3d['data']['points']
    marker_names = c3d['parameters']['POINT']['LABELS']['value']
    num_markers = points.shape[1]
    num_frames = points.shape[2]

    # nom du CSV en fonction du fichier C3D
    csv_filename = f"{nom}.csv"

    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Frame", "Marker", "Marker_Name", "X", "Y", "Z", "Valid"])

        for frame in range(num_frames):
            for marker in range(num_markers):
                x = points[0, marker, frame]
                y = points[1, marker, frame]
                z = points[2, marker, frame]
                valid = points[3, marker, frame]
                name = marker_names[marker]

                csv_writer.writerow([frame + 1, marker + 1, name, x, y, z, valid])

    print(f"✔ CSV généré : {csv_filename}")
