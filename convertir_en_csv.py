import ezc3d
import csv


c3d_Chrono250 = ezc3d.c3d("data/Chrono250_c3d.c3d")
c3d_Chrono300 = ezc3d.c3d("data/Chrono300_c3d.c3d")
c3d_Chrono500 = ezc3d.c3d("data/Chrono350_c3d.c3d")
c3d_Route250 = ezc3d.c3d("data/Route250_c3d.c3d")
c3d_Route300 = ezc3d.c3d("data/Route300_c3d.c3d")
c3d_Route500 = ezc3d.c3d("data/Route350_c3d.c3d")

liste_fichiers = [c3d_Chrono250, c3d_Chrono300, c3d_Chrono500, c3d_Route250, c3d_Route300,
                  c3d_Route500]

for c3d in liste_fichiers:
    points = c3d['data']['points']  # Données des marqueurs
    marker_names = c3d['parameters']['POINT']['LABELS']['value']
    num_markers = points.shape[1]
    num_frames = points.shape[2]

    with open("markers.csv", "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Frame", "Marker", "Marker_Name", "X", "Y", "Z", "Valid"])  # En-têtes

        # Boucle sur toutes les trames et tous les marqueurs
        for frame in range(num_frames):
            for marker in range(num_markers):
                x = points[0, marker, frame]
                y = points[1, marker, frame]
                z = points[2, marker, frame]
                valid = points[3, marker, frame]
                name = marker_names[marker]
                csv_writer.writerow([frame + 1, marker + 1, name, x, y, z, valid])
