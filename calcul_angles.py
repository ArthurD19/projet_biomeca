import numpy as np
import pandas as pd

from calculer_centres_articulaires import df_chrono250
from calculer_centres_articulaires import df_chrono300
from calculer_centres_articulaires import df_chrono350
from calculer_centres_articulaires import df_route250
from calculer_centres_articulaires import df_route300
from calculer_centres_articulaires import df_route350

# Lecture des fichiers CSV

df_Chrono250 = pd.read_csv("Chrono250.csv")
df_Chrono300 = pd.read_csv("Chrono300.csv")
df_Chrono350 = pd.read_csv("Chrono350.csv")
df_Route250 = pd.read_csv("Route250.csv")
df_Route300 = pd.read_csv("Route300.csv")
df_Route350 = pd.read_csv("Route350.csv")

#################################################################################################

# FONCTION UTILES


def calcul_distance(p1, p2):
    """Calcul de la distance entre deux points p1 et p2."""
    return np.sqrt((p2["X"] - p1["X"]) ** 2 + (p2["Z"] - p1["Z"]) ** 2 + (p2["Y"] - p1["Y"]) ** 2)


def calcul_angle(p1, p2, articulation):
    """
    Calcule l'angle entre les côtés du triangle formé par les points p1, p2, articulation.
    Calcule l'angle au niveau de articulation

    p1, p2, articulation : points avec coordonées de type (X, Y, Z)
    """
    # Calcul des longueurs des côtés
    a = calcul_distance(p2, articulation)  # Distance entre p2 et articulation
    b = calcul_distance(p1, articulation)  # Distance entre p1 et articulation
    c = calcul_distance(p1, p2)  # Distance entre p1 et p2 (opposé à l'angle de l'articulation)

    # Loi des cosinus : cos(alpha)) = (a^2 + b^2 - c^2) / (2ab)
    cos_alpha = (a**2 + b**2 - c**2) / (2 * a * b)

    # Calcul de l'angle en radians
    angle_alpha_radians = np.arccos(cos_alpha)

    return angle_alpha_radians * 180 / np.pi


##################################################################################################

# On commence par récupérer les points qui vont nous être utiles

liste_points_utiles = ["pRightToe", "pLeftToe", "pRightAcromion", "pLeftAcromion", "pPX"]
# On a récupéré les points correspondants aux orteils, aux épaules et au sternum

df_Chrono250_utiles = df_Chrono250[df_Chrono250["Marker_Name"].isin(liste_points_utiles)]
df_Chrono300_utiles = df_Chrono300[df_Chrono300["Marker_Name"].isin(liste_points_utiles)]
df_Chrono350_utiles = df_Chrono350[df_Chrono350["Marker_Name"].isin(liste_points_utiles)]
df_Route250_utiles = df_Route250[df_Route250["Marker_Name"].isin(liste_points_utiles)]
df_Route300_utiles = df_Route300[df_Route300["Marker_Name"].isin(liste_points_utiles)]
df_Route350_utiles = df_Route350[df_Route350["Marker_Name"].isin(liste_points_utiles)]

# On crée les dataframe complets
df_Chrono250_complet = (
    pd.concat([df_Chrono250_utiles, df_chrono250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_Chrono300_complet = (
    pd.concat([df_Chrono300_utiles, df_chrono300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_Chrono350_complet = (
    pd.concat([df_Chrono350_utiles, df_chrono350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_Route250_complet = (
    pd.concat([df_Route250_utiles, df_route250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_Route300_complet = (
    pd.concat([df_Route300_utiles, df_route300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_Route350_complet = (
    pd.concat([df_Route350_utiles, df_route350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_Chrono250_complet = df_Chrono250_complet.loc[:, ~df_Chrono250_complet.columns.duplicated()]
df_Chrono300_complet = df_Chrono300_complet.loc[:, ~df_Chrono300_complet.columns.duplicated()]
df_Chrono350_complet = df_Chrono350_complet.loc[:, ~df_Chrono350_complet.columns.duplicated()]
df_Route250_complet = df_Route250_complet.loc[:, ~df_Route250_complet.columns.duplicated()]
df_Route300_complet = df_Route300_complet.loc[:, ~df_Route300_complet.columns.duplicated()]
df_Route350_complet = df_Route350_complet.loc[:, ~df_Route350_complet.columns.duplicated()]

#####################################################################################

# On crée un dataframe pour y mettre les angles

df_angles_Chrono250 = pd.DataFrame(columns=["Frame", "Articulation", "Angle"])
df_angles_Chrono300 = pd.DataFrame(columns=["Frame", "Articulation", "Angle"])
df_angles_Chrono350 = pd.DataFrame(columns=["Frame", "Articulation", "Angle"])
df_angles_Route250 = pd.DataFrame(columns=["Frame", "Articulation", "Angle"])
df_angles_Route300 = pd.DataFrame(columns=["Frame", "Articulation", "Angle"])
df_angles_Route350 = pd.DataFrame(columns=["Frame", "Articulation", "Angle"])

#####################################################################################

# On commence par Chrono250

for frame in range(1, max(df_Chrono250_complet["Frame"]) + 1):
    df_frame_i = df_Chrono250_complet[df_Chrono250_complet["Frame"] == frame]

    # Récupération des coordonnées de chaque point

    coord_x_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["X"]
    coord_y_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Y"]
    coord_z_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Z"]
    coord_sternum = {
        "X": float(coord_x_sternum.iloc[0]),
        "Z": float(coord_z_sternum.iloc[0]),
        "Y": float(coord_y_sternum.iloc[0]),
    }

    coord_x_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["X"]
    coord_y_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Y"]
    coord_z_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Z"]
    coord_epaule_d = {
        "X": float(coord_x_epaule_d.iloc[0]),
        "Y": float(coord_y_epaule_d.iloc[0]),
        "Z": float(coord_z_epaule_d.iloc[0]),
    }

    coord_x_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["X"]
    coord_y_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Y"]
    coord_z_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Z"]
    coord_epaule_g = {
        "X": float(coord_x_epaule_g.iloc[0]),
        "Y": float(coord_y_epaule_g.iloc[0]),
        "Z": float(coord_z_epaule_g.iloc[0]),
    }

    coord_x_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["X"]
    coord_y_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Y"]
    coord_z_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Z"]
    coord_coude_d = {
        "X": float(coord_x_coude_d.iloc[0]),
        "Y": float(coord_y_coude_d.iloc[0]),
        "Z": float(coord_z_coude_d.iloc[0]),
    }

    coord_x_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["X"]
    coord_y_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Y"]
    coord_z_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Z"]
    coord_coude_g = {
        "X": float(coord_x_coude_g.iloc[0]),
        "Y": float(coord_y_coude_g.iloc[0]),
        "Z": float(coord_z_coude_g.iloc[0]),
    }

    coord_x_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["X"]
    coord_y_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Y"]
    coord_z_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Z"]
    coord_hanche_d = {
        "X": float(coord_x_hanche_d.iloc[0]),
        "Y": float(coord_y_hanche_d.iloc[0]),
        "Z": float(coord_z_hanche_d.iloc[0]),
    }

    coord_x_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["X"]
    coord_y_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Y"]
    coord_z_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Z"]
    coord_hanche_g = {
        "X": float(coord_x_hanche_g.iloc[0]),
        "Y": float(coord_y_hanche_g.iloc[0]),
        "Z": float(coord_z_hanche_g.iloc[0]),
    }

    coord_x_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["X"]
    coord_y_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Y"]
    coord_z_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Z"]
    coord_genou_d = {
        "X": float(coord_x_genou_d.iloc[0]),
        "Y": float(coord_y_genou_d.iloc[0]),
        "Z": float(coord_z_genou_d.iloc[0]),
    }

    coord_x_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["X"]
    coord_y_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Y"]
    coord_z_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Z"]
    coord_genou_g = {
        "X": float(coord_x_genou_g.iloc[0]),
        "Y": float(coord_y_genou_g.iloc[0]),
        "Z": float(coord_z_genou_g.iloc[0]),
    }

    coord_x_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["X"]
    coord_y_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Y"]
    coord_z_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Z"]
    coord_cheville_d = {
        "X": float(coord_x_cheville_d.iloc[0]),
        "Y": float(coord_y_cheville_d.iloc[0]),
        "Z": float(coord_z_cheville_d.iloc[0]),
    }

    coord_x_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["X"]
    coord_y_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Y"]
    coord_z_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Z"]
    coord_cheville_g = {
        "X": float(coord_x_cheville_g.iloc[0]),
        "Y": float(coord_y_cheville_g.iloc[0]),
        "Z": float(coord_z_cheville_g.iloc[0]),
    }

    coord_x_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["X"]
    coord_y_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Y"]
    coord_z_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Z"]
    coord_orteil_d = {
        "X": float(coord_x_orteil_d.iloc[0]),
        "Y": float(coord_y_orteil_d.iloc[0]),
        "Z": float(coord_z_orteil_d.iloc[0]),
    }

    coord_x_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["X"]
    coord_y_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Y"]
    coord_z_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Z"]
    coord_orteil_g = {
        "X": float(coord_x_orteil_g.iloc[0]),
        "Y": float(coord_y_orteil_g.iloc[0]),
        "Z": float(coord_z_orteil_g.iloc[0]),
    }

    # Calcule des angles pour chaque articulation

    angle_hanche_droite = calcul_angle(coord_genou_d, coord_sternum, articulation=coord_hanche_d)
    angle_hanche_gauche = calcul_angle(coord_genou_g, coord_sternum, articulation=coord_hanche_g)

    angle_genou_droit = calcul_angle(coord_cheville_d, coord_hanche_d, articulation=coord_genou_d)
    angle_genou_gauche = calcul_angle(coord_cheville_g, coord_hanche_g, articulation=coord_genou_g)

    angle_epaule_droite = calcul_angle(coord_sternum, coord_coude_d, articulation=coord_epaule_d)
    angle_epaule_gauche = calcul_angle(coord_sternum, coord_coude_g, articulation=coord_epaule_g)

    angle_cheville_droite = calcul_angle(coord_genou_d, coord_orteil_d, articulation=coord_cheville_d)
    angle_cheville_gauche = calcul_angle(coord_genou_g, coord_orteil_g, articulation=coord_cheville_g)

    # On met à jour le dataframe avec ces angles

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche droite",
        "Angle": angle_hanche_droite,
    }

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche gauche",
        "Angle": angle_hanche_gauche,
    }

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou droit",
        "Angle": angle_genou_droit,
    }

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou gauche",
        "Angle": angle_genou_gauche,
    }

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule droite",
        "Angle": angle_epaule_droite,
    }

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule gauche",
        "Angle": angle_epaule_gauche,
    }

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville droite",
        "Angle": angle_cheville_droite,
    }

    df_angles_Chrono250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville gauche",
        "Angle": angle_cheville_gauche,
    }

#####################################################################################

# On fait de même pour Chrono300

for frame in range(1, max(df_Chrono300_complet["Frame"]) + 1):
    df_frame_i = df_Chrono300_complet[df_Chrono300_complet["Frame"] == frame]

    # Récupération des coordonnées de chaque point

    coord_x_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["X"]
    coord_y_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Y"]
    coord_z_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Z"]
    coord_sternum = {
        "X": float(coord_x_sternum.iloc[0]),
        "Z": float(coord_z_sternum.iloc[0]),
        "Y": float(coord_y_sternum.iloc[0]),
    }

    coord_x_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["X"]
    coord_y_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Y"]
    coord_z_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Z"]
    coord_epaule_d = {
        "X": float(coord_x_epaule_d.iloc[0]),
        "Y": float(coord_y_epaule_d.iloc[0]),
        "Z": float(coord_z_epaule_d.iloc[0]),
    }

    coord_x_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["X"]
    coord_y_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Y"]
    coord_z_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Z"]
    coord_epaule_g = {
        "X": float(coord_x_epaule_g.iloc[0]),
        "Y": float(coord_y_epaule_g.iloc[0]),
        "Z": float(coord_z_epaule_g.iloc[0]),
    }

    coord_x_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["X"]
    coord_y_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Y"]
    coord_z_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Z"]
    coord_coude_d = {
        "X": float(coord_x_coude_d.iloc[0]),
        "Y": float(coord_y_coude_d.iloc[0]),
        "Z": float(coord_z_coude_d.iloc[0]),
    }

    coord_x_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["X"]
    coord_y_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Y"]
    coord_z_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Z"]
    coord_coude_g = {
        "X": float(coord_x_coude_g.iloc[0]),
        "Y": float(coord_y_coude_g.iloc[0]),
        "Z": float(coord_z_coude_g.iloc[0]),
    }

    coord_x_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["X"]
    coord_y_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Y"]
    coord_z_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Z"]
    coord_hanche_d = {
        "X": float(coord_x_hanche_d.iloc[0]),
        "Y": float(coord_y_hanche_d.iloc[0]),
        "Z": float(coord_z_hanche_d.iloc[0]),
    }

    coord_x_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["X"]
    coord_y_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Y"]
    coord_z_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Z"]
    coord_hanche_g = {
        "X": float(coord_x_hanche_g.iloc[0]),
        "Y": float(coord_y_hanche_g.iloc[0]),
        "Z": float(coord_z_hanche_g.iloc[0]),
    }

    coord_x_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["X"]
    coord_y_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Y"]
    coord_z_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Z"]
    coord_genou_d = {
        "X": float(coord_x_genou_d.iloc[0]),
        "Y": float(coord_y_genou_d.iloc[0]),
        "Z": float(coord_z_genou_d.iloc[0]),
    }

    coord_x_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["X"]
    coord_y_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Y"]
    coord_z_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Z"]
    coord_genou_g = {
        "X": float(coord_x_genou_g.iloc[0]),
        "Y": float(coord_y_genou_g.iloc[0]),
        "Z": float(coord_z_genou_g.iloc[0]),
    }

    coord_x_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["X"]
    coord_y_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Y"]
    coord_z_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Z"]
    coord_cheville_d = {
        "X": float(coord_x_cheville_d.iloc[0]),
        "Y": float(coord_y_cheville_d.iloc[0]),
        "Z": float(coord_z_cheville_d.iloc[0]),
    }

    coord_x_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["X"]
    coord_y_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Y"]
    coord_z_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Z"]
    coord_cheville_g = {
        "X": float(coord_x_cheville_g.iloc[0]),
        "Y": float(coord_y_cheville_g.iloc[0]),
        "Z": float(coord_z_cheville_g.iloc[0]),
    }

    coord_x_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["X"]
    coord_y_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Y"]
    coord_z_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Z"]
    coord_orteil_d = {
        "X": float(coord_x_orteil_d.iloc[0]),
        "Y": float(coord_y_orteil_d.iloc[0]),
        "Z": float(coord_z_orteil_d.iloc[0]),
    }

    coord_x_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["X"]
    coord_y_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Y"]
    coord_z_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Z"]
    coord_orteil_g = {
        "X": float(coord_x_orteil_g.iloc[0]),
        "Y": float(coord_y_orteil_g.iloc[0]),
        "Z": float(coord_z_orteil_g.iloc[0]),
    }

    # Calcule des angles pour chaque articulation

    angle_hanche_droite = calcul_angle(coord_genou_d, coord_sternum, articulation=coord_hanche_d)
    angle_hanche_gauche = calcul_angle(coord_genou_g, coord_sternum, articulation=coord_hanche_g)

    angle_genou_droit = calcul_angle(coord_cheville_d, coord_hanche_d, articulation=coord_genou_d)
    angle_genou_gauche = calcul_angle(coord_cheville_g, coord_hanche_g, articulation=coord_genou_g)

    angle_epaule_droite = calcul_angle(coord_sternum, coord_coude_d, articulation=coord_epaule_d)
    angle_epaule_gauche = calcul_angle(coord_sternum, coord_coude_g, articulation=coord_epaule_g)

    angle_cheville_droite = calcul_angle(coord_genou_d, coord_orteil_d, articulation=coord_cheville_d)
    angle_cheville_gauche = calcul_angle(coord_genou_g, coord_orteil_g, articulation=coord_cheville_g)

    # On met à jour le dataframe avec ces angles

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Hanche droite",
        "Angle": angle_hanche_droite,
    }

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Hanche gauche",
        "Angle": angle_hanche_gauche,
    }

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Genou droit",
        "Angle": angle_genou_droit,
    }

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Genou gauche",
        "Angle": angle_genou_gauche,
    }

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Epaule droite",
        "Angle": angle_epaule_droite,
    }

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Epaule gauche",
        "Angle": angle_epaule_gauche,
    }

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Cheville droite",
        "Angle": angle_cheville_droite,
    }

    df_angles_Chrono300.loc[len(df_angles_Chrono300)] = {
        "Frame": frame,
        "Articulation": "Cheville gauche",
        "Angle": angle_cheville_gauche,
    }

#####################################################################################

# Puis avec Chrono350

for frame in range(1, max(df_Chrono350_complet["Frame"]) + 1):
    df_frame_i = df_Chrono350_complet[df_Chrono350_complet["Frame"] == frame]

    # Récupération des coordonnées de chaque point

    coord_x_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["X"]
    coord_y_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Y"]
    coord_z_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Z"]
    coord_sternum = {
        "X": float(coord_x_sternum.iloc[0]),
        "Z": float(coord_z_sternum.iloc[0]),
        "Y": float(coord_y_sternum.iloc[0]),
    }

    coord_x_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["X"]
    coord_y_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Y"]
    coord_z_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Z"]
    coord_epaule_d = {
        "X": float(coord_x_epaule_d.iloc[0]),
        "Y": float(coord_y_epaule_d.iloc[0]),
        "Z": float(coord_z_epaule_d.iloc[0]),
    }

    coord_x_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["X"]
    coord_y_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Y"]
    coord_z_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Z"]
    coord_epaule_g = {
        "X": float(coord_x_epaule_g.iloc[0]),
        "Y": float(coord_y_epaule_g.iloc[0]),
        "Z": float(coord_z_epaule_g.iloc[0]),
    }

    coord_x_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["X"]
    coord_y_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Y"]
    coord_z_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Z"]
    coord_coude_d = {
        "X": float(coord_x_coude_d.iloc[0]),
        "Y": float(coord_y_coude_d.iloc[0]),
        "Z": float(coord_z_coude_d.iloc[0]),
    }

    coord_x_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["X"]
    coord_y_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Y"]
    coord_z_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Z"]
    coord_coude_g = {
        "X": float(coord_x_coude_g.iloc[0]),
        "Y": float(coord_y_coude_g.iloc[0]),
        "Z": float(coord_z_coude_g.iloc[0]),
    }

    coord_x_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["X"]
    coord_y_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Y"]
    coord_z_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Z"]
    coord_hanche_d = {
        "X": float(coord_x_hanche_d.iloc[0]),
        "Y": float(coord_y_hanche_d.iloc[0]),
        "Z": float(coord_z_hanche_d.iloc[0]),
    }

    coord_x_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["X"]
    coord_y_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Y"]
    coord_z_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Z"]
    coord_hanche_g = {
        "X": float(coord_x_hanche_g.iloc[0]),
        "Y": float(coord_y_hanche_g.iloc[0]),
        "Z": float(coord_z_hanche_g.iloc[0]),
    }

    coord_x_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["X"]
    coord_y_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Y"]
    coord_z_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Z"]
    coord_genou_d = {
        "X": float(coord_x_genou_d.iloc[0]),
        "Y": float(coord_y_genou_d.iloc[0]),
        "Z": float(coord_z_genou_d.iloc[0]),
    }

    coord_x_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["X"]
    coord_y_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Y"]
    coord_z_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Z"]
    coord_genou_g = {
        "X": float(coord_x_genou_g.iloc[0]),
        "Y": float(coord_y_genou_g.iloc[0]),
        "Z": float(coord_z_genou_g.iloc[0]),
    }

    coord_x_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["X"]
    coord_y_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Y"]
    coord_z_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Z"]
    coord_cheville_d = {
        "X": float(coord_x_cheville_d.iloc[0]),
        "Y": float(coord_y_cheville_d.iloc[0]),
        "Z": float(coord_z_cheville_d.iloc[0]),
    }

    coord_x_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["X"]
    coord_y_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Y"]
    coord_z_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Z"]
    coord_cheville_g = {
        "X": float(coord_x_cheville_g.iloc[0]),
        "Y": float(coord_y_cheville_g.iloc[0]),
        "Z": float(coord_z_cheville_g.iloc[0]),
    }

    coord_x_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["X"]
    coord_y_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Y"]
    coord_z_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Z"]
    coord_orteil_d = {
        "X": float(coord_x_orteil_d.iloc[0]),
        "Y": float(coord_y_orteil_d.iloc[0]),
        "Z": float(coord_z_orteil_d.iloc[0]),
    }

    coord_x_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["X"]
    coord_y_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Y"]
    coord_z_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Z"]
    coord_orteil_g = {
        "X": float(coord_x_orteil_g.iloc[0]),
        "Y": float(coord_y_orteil_g.iloc[0]),
        "Z": float(coord_z_orteil_g.iloc[0]),
    }

    # Calcule des angles pour chaque articulation

    angle_hanche_droite = calcul_angle(coord_genou_d, coord_sternum, articulation=coord_hanche_d)
    angle_hanche_gauche = calcul_angle(coord_genou_g, coord_sternum, articulation=coord_hanche_g)

    angle_genou_droit = calcul_angle(coord_cheville_d, coord_hanche_d, articulation=coord_genou_d)
    angle_genou_gauche = calcul_angle(coord_cheville_g, coord_hanche_g, articulation=coord_genou_g)

    angle_epaule_droite = calcul_angle(coord_sternum, coord_coude_d, articulation=coord_epaule_d)
    angle_epaule_gauche = calcul_angle(coord_sternum, coord_coude_g, articulation=coord_epaule_g)

    angle_cheville_droite = calcul_angle(coord_genou_d, coord_orteil_d, articulation=coord_cheville_d)
    angle_cheville_gauche = calcul_angle(coord_genou_g, coord_orteil_g, articulation=coord_cheville_g)

    # On met à jour le dataframe avec ces angles

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche droite",
        "Angle": angle_hanche_droite,
    }

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche gauche",
        "Angle": angle_hanche_gauche,
    }

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou droit",
        "Angle": angle_genou_droit,
    }

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou gauche",
        "Angle": angle_genou_gauche,
    }

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule droite",
        "Angle": angle_epaule_droite,
    }

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule gauche",
        "Angle": angle_epaule_gauche,
    }

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville droite",
        "Angle": angle_cheville_droite,
    }

    df_angles_Chrono350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville gauche",
        "Angle": angle_cheville_gauche,
    }

#####################################################################################

# On passe maintenant à Route250

for frame in range(1, max(df_Route250_complet["Frame"]) + 1):
    df_frame_i = df_Route250_complet[df_Route250_complet["Frame"] == frame]

    # Récupération des coordonnées de chaque point

    coord_x_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["X"]
    coord_y_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Y"]
    coord_z_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Z"]
    coord_sternum = {
        "X": float(coord_x_sternum.iloc[0]),
        "Z": float(coord_z_sternum.iloc[0]),
        "Y": float(coord_y_sternum.iloc[0]),
    }

    coord_x_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["X"]
    coord_y_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Y"]
    coord_z_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Z"]
    coord_epaule_d = {
        "X": float(coord_x_epaule_d.iloc[0]),
        "Y": float(coord_y_epaule_d.iloc[0]),
        "Z": float(coord_z_epaule_d.iloc[0]),
    }

    coord_x_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["X"]
    coord_y_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Y"]
    coord_z_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Z"]
    coord_epaule_g = {
        "X": float(coord_x_epaule_g.iloc[0]),
        "Y": float(coord_y_epaule_g.iloc[0]),
        "Z": float(coord_z_epaule_g.iloc[0]),
    }

    coord_x_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["X"]
    coord_y_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Y"]
    coord_z_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Z"]
    coord_coude_d = {
        "X": float(coord_x_coude_d.iloc[0]),
        "Y": float(coord_y_coude_d.iloc[0]),
        "Z": float(coord_z_coude_d.iloc[0]),
    }

    coord_x_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["X"]
    coord_y_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Y"]
    coord_z_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Z"]
    coord_coude_g = {
        "X": float(coord_x_coude_g.iloc[0]),
        "Y": float(coord_y_coude_g.iloc[0]),
        "Z": float(coord_z_coude_g.iloc[0]),
    }

    coord_x_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["X"]
    coord_y_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Y"]
    coord_z_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Z"]
    coord_hanche_d = {
        "X": float(coord_x_hanche_d.iloc[0]),
        "Y": float(coord_y_hanche_d.iloc[0]),
        "Z": float(coord_z_hanche_d.iloc[0]),
    }

    coord_x_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["X"]
    coord_y_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Y"]
    coord_z_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Z"]
    coord_hanche_g = {
        "X": float(coord_x_hanche_g.iloc[0]),
        "Y": float(coord_y_hanche_g.iloc[0]),
        "Z": float(coord_z_hanche_g.iloc[0]),
    }

    coord_x_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["X"]
    coord_y_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Y"]
    coord_z_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Z"]
    coord_genou_d = {
        "X": float(coord_x_genou_d.iloc[0]),
        "Y": float(coord_y_genou_d.iloc[0]),
        "Z": float(coord_z_genou_d.iloc[0]),
    }

    coord_x_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["X"]
    coord_y_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Y"]
    coord_z_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Z"]
    coord_genou_g = {
        "X": float(coord_x_genou_g.iloc[0]),
        "Y": float(coord_y_genou_g.iloc[0]),
        "Z": float(coord_z_genou_g.iloc[0]),
    }

    coord_x_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["X"]
    coord_y_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Y"]
    coord_z_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Z"]
    coord_cheville_d = {
        "X": float(coord_x_cheville_d.iloc[0]),
        "Y": float(coord_y_cheville_d.iloc[0]),
        "Z": float(coord_z_cheville_d.iloc[0]),
    }

    coord_x_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["X"]
    coord_y_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Y"]
    coord_z_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Z"]
    coord_cheville_g = {
        "X": float(coord_x_cheville_g.iloc[0]),
        "Y": float(coord_y_cheville_g.iloc[0]),
        "Z": float(coord_z_cheville_g.iloc[0]),
    }

    coord_x_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["X"]
    coord_y_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Y"]
    coord_z_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Z"]
    coord_orteil_d = {
        "X": float(coord_x_orteil_d.iloc[0]),
        "Y": float(coord_y_orteil_d.iloc[0]),
        "Z": float(coord_z_orteil_d.iloc[0]),
    }

    coord_x_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["X"]
    coord_y_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Y"]
    coord_z_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Z"]
    coord_orteil_g = {
        "X": float(coord_x_orteil_g.iloc[0]),
        "Y": float(coord_y_orteil_g.iloc[0]),
        "Z": float(coord_z_orteil_g.iloc[0]),
    }

    # Calcule des angles pour chaque articulation

    angle_hanche_droite = calcul_angle(coord_genou_d, coord_sternum, articulation=coord_hanche_d)
    angle_hanche_gauche = calcul_angle(coord_genou_g, coord_sternum, articulation=coord_hanche_g)

    angle_genou_droit = calcul_angle(coord_cheville_d, coord_hanche_d, articulation=coord_genou_d)
    angle_genou_gauche = calcul_angle(coord_cheville_g, coord_hanche_g, articulation=coord_genou_g)

    angle_epaule_droite = calcul_angle(coord_sternum, coord_coude_d, articulation=coord_epaule_d)
    angle_epaule_gauche = calcul_angle(coord_sternum, coord_coude_g, articulation=coord_epaule_g)

    angle_cheville_droite = calcul_angle(coord_genou_d, coord_orteil_d, articulation=coord_cheville_d)
    angle_cheville_gauche = calcul_angle(coord_genou_g, coord_orteil_g, articulation=coord_cheville_g)

    # On met à jour le dataframe avec ces angles

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche droite",
        "Angle": angle_hanche_droite,
    }

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche gauche",
        "Angle": angle_hanche_gauche,
    }

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou droit",
        "Angle": angle_genou_droit,
    }

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou gauche",
        "Angle": angle_genou_gauche,
    }

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule droite",
        "Angle": angle_epaule_droite,
    }

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule gauche",
        "Angle": angle_epaule_gauche,
    }

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville droite",
        "Angle": angle_cheville_droite,
    }

    df_angles_Route250.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville gauche",
        "Angle": angle_cheville_gauche,
    }

#####################################################################################

# On fait mainteant Route300

for frame in range(1, max(df_Route300_complet["Frame"]) + 1):
    df_frame_i = df_Route300_complet[df_Route300_complet["Frame"] == frame]

    # Récupération des coordonnées de chaque point

    coord_x_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["X"]
    coord_y_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Y"]
    coord_z_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Z"]
    coord_sternum = {
        "X": float(coord_x_sternum.iloc[0]),
        "Z": float(coord_z_sternum.iloc[0]),
        "Y": float(coord_y_sternum.iloc[0]),
    }

    coord_x_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["X"]
    coord_y_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Y"]
    coord_z_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Z"]
    coord_epaule_d = {
        "X": float(coord_x_epaule_d.iloc[0]),
        "Y": float(coord_y_epaule_d.iloc[0]),
        "Z": float(coord_z_epaule_d.iloc[0]),
    }

    coord_x_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["X"]
    coord_y_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Y"]
    coord_z_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Z"]
    coord_epaule_g = {
        "X": float(coord_x_epaule_g.iloc[0]),
        "Y": float(coord_y_epaule_g.iloc[0]),
        "Z": float(coord_z_epaule_g.iloc[0]),
    }

    coord_x_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["X"]
    coord_y_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Y"]
    coord_z_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Z"]
    coord_coude_d = {
        "X": float(coord_x_coude_d.iloc[0]),
        "Y": float(coord_y_coude_d.iloc[0]),
        "Z": float(coord_z_coude_d.iloc[0]),
    }

    coord_x_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["X"]
    coord_y_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Y"]
    coord_z_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Z"]
    coord_coude_g = {
        "X": float(coord_x_coude_g.iloc[0]),
        "Y": float(coord_y_coude_g.iloc[0]),
        "Z": float(coord_z_coude_g.iloc[0]),
    }

    coord_x_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["X"]
    coord_y_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Y"]
    coord_z_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Z"]
    coord_hanche_d = {
        "X": float(coord_x_hanche_d.iloc[0]),
        "Y": float(coord_y_hanche_d.iloc[0]),
        "Z": float(coord_z_hanche_d.iloc[0]),
    }

    coord_x_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["X"]
    coord_y_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Y"]
    coord_z_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Z"]
    coord_hanche_g = {
        "X": float(coord_x_hanche_g.iloc[0]),
        "Y": float(coord_y_hanche_g.iloc[0]),
        "Z": float(coord_z_hanche_g.iloc[0]),
    }

    coord_x_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["X"]
    coord_y_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Y"]
    coord_z_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Z"]
    coord_genou_d = {
        "X": float(coord_x_genou_d.iloc[0]),
        "Y": float(coord_y_genou_d.iloc[0]),
        "Z": float(coord_z_genou_d.iloc[0]),
    }

    coord_x_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["X"]
    coord_y_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Y"]
    coord_z_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Z"]
    coord_genou_g = {
        "X": float(coord_x_genou_g.iloc[0]),
        "Y": float(coord_y_genou_g.iloc[0]),
        "Z": float(coord_z_genou_g.iloc[0]),
    }

    coord_x_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["X"]
    coord_y_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Y"]
    coord_z_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Z"]
    coord_cheville_d = {
        "X": float(coord_x_cheville_d.iloc[0]),
        "Y": float(coord_y_cheville_d.iloc[0]),
        "Z": float(coord_z_cheville_d.iloc[0]),
    }

    coord_x_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["X"]
    coord_y_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Y"]
    coord_z_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Z"]
    coord_cheville_g = {
        "X": float(coord_x_cheville_g.iloc[0]),
        "Y": float(coord_y_cheville_g.iloc[0]),
        "Z": float(coord_z_cheville_g.iloc[0]),
    }

    coord_x_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["X"]
    coord_y_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Y"]
    coord_z_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Z"]
    coord_orteil_d = {
        "X": float(coord_x_orteil_d.iloc[0]),
        "Y": float(coord_y_orteil_d.iloc[0]),
        "Z": float(coord_z_orteil_d.iloc[0]),
    }

    coord_x_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["X"]
    coord_y_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Y"]
    coord_z_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Z"]
    coord_orteil_g = {
        "X": float(coord_x_orteil_g.iloc[0]),
        "Y": float(coord_y_orteil_g.iloc[0]),
        "Z": float(coord_z_orteil_g.iloc[0]),
    }

    # Calcule des angles pour chaque articulation

    angle_hanche_droite = calcul_angle(coord_genou_d, coord_sternum, articulation=coord_hanche_d)
    angle_hanche_gauche = calcul_angle(coord_genou_g, coord_sternum, articulation=coord_hanche_g)

    angle_genou_droit = calcul_angle(coord_cheville_d, coord_hanche_d, articulation=coord_genou_d)
    angle_genou_gauche = calcul_angle(coord_cheville_g, coord_hanche_g, articulation=coord_genou_g)

    angle_epaule_droite = calcul_angle(coord_sternum, coord_coude_d, articulation=coord_epaule_d)
    angle_epaule_gauche = calcul_angle(coord_sternum, coord_coude_g, articulation=coord_epaule_g)

    angle_cheville_droite = calcul_angle(coord_genou_d, coord_orteil_d, articulation=coord_cheville_d)
    angle_cheville_gauche = calcul_angle(coord_genou_g, coord_orteil_g, articulation=coord_cheville_g)

    # On met à jour le dataframe avec ces angles

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche droite",
        "Angle": angle_hanche_droite,
    }

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche gauche",
        "Angle": angle_hanche_gauche,
    }

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou droit",
        "Angle": angle_genou_droit,
    }

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou gauche",
        "Angle": angle_genou_gauche,
    }

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule droite",
        "Angle": angle_epaule_droite,
    }

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule gauche",
        "Angle": angle_epaule_gauche,
    }

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville droite",
        "Angle": angle_cheville_droite,
    }

    df_angles_Route300.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville gauche",
        "Angle": angle_cheville_gauche,
    }

#####################################################################################

# On finit par Route350

for frame in range(1, max(df_Route350_complet["Frame"]) + 1):
    df_frame_i = df_Route350_complet[df_Route350_complet["Frame"] == frame]

    # Récupération des coordonnées de chaque point

    coord_x_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["X"]
    coord_y_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Y"]
    coord_z_sternum = df_frame_i[df_frame_i["Marker_Name"] == "pPX"]["Z"]
    coord_sternum = {
        "X": float(coord_x_sternum.iloc[0]),
        "Z": float(coord_z_sternum.iloc[0]),
        "Y": float(coord_y_sternum.iloc[0]),
    }

    coord_x_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["X"]
    coord_y_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Y"]
    coord_z_epaule_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightAcromion"]["Z"]
    coord_epaule_d = {
        "X": float(coord_x_epaule_d.iloc[0]),
        "Y": float(coord_y_epaule_d.iloc[0]),
        "Z": float(coord_z_epaule_d.iloc[0]),
    }

    coord_x_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["X"]
    coord_y_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Y"]
    coord_z_epaule_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftAcromion"]["Z"]
    coord_epaule_g = {
        "X": float(coord_x_epaule_g.iloc[0]),
        "Y": float(coord_y_epaule_g.iloc[0]),
        "Z": float(coord_z_epaule_g.iloc[0]),
    }

    coord_x_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["X"]
    coord_y_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Y"]
    coord_z_coude_d = df_frame_i[df_frame_i["Marker_Name"] == "Coude droit"]["Z"]
    coord_coude_d = {
        "X": float(coord_x_coude_d.iloc[0]),
        "Y": float(coord_y_coude_d.iloc[0]),
        "Z": float(coord_z_coude_d.iloc[0]),
    }

    coord_x_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["X"]
    coord_y_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Y"]
    coord_z_coude_g = df_frame_i[df_frame_i["Marker_Name"] == "Coude gauche"]["Z"]
    coord_coude_g = {
        "X": float(coord_x_coude_g.iloc[0]),
        "Y": float(coord_y_coude_g.iloc[0]),
        "Z": float(coord_z_coude_g.iloc[0]),
    }

    coord_x_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["X"]
    coord_y_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Y"]
    coord_z_hanche_d = df_frame_i[df_frame_i["Marker_Name"] == "Hanche droite"]["Z"]
    coord_hanche_d = {
        "X": float(coord_x_hanche_d.iloc[0]),
        "Y": float(coord_y_hanche_d.iloc[0]),
        "Z": float(coord_z_hanche_d.iloc[0]),
    }

    coord_x_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["X"]
    coord_y_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Y"]
    coord_z_hanche_g = df_frame_i[df_frame_i["Marker_Name"] == "Hanche gauche"]["Z"]
    coord_hanche_g = {
        "X": float(coord_x_hanche_g.iloc[0]),
        "Y": float(coord_y_hanche_g.iloc[0]),
        "Z": float(coord_z_hanche_g.iloc[0]),
    }

    coord_x_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["X"]
    coord_y_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Y"]
    coord_z_genou_d = df_frame_i[df_frame_i["Marker_Name"] == "Genou droit"]["Z"]
    coord_genou_d = {
        "X": float(coord_x_genou_d.iloc[0]),
        "Y": float(coord_y_genou_d.iloc[0]),
        "Z": float(coord_z_genou_d.iloc[0]),
    }

    coord_x_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["X"]
    coord_y_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Y"]
    coord_z_genou_g = df_frame_i[df_frame_i["Marker_Name"] == "Genou gauche"]["Z"]
    coord_genou_g = {
        "X": float(coord_x_genou_g.iloc[0]),
        "Y": float(coord_y_genou_g.iloc[0]),
        "Z": float(coord_z_genou_g.iloc[0]),
    }

    coord_x_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["X"]
    coord_y_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Y"]
    coord_z_cheville_d = df_frame_i[df_frame_i["Marker_Name"] == "Cheville droite"]["Z"]
    coord_cheville_d = {
        "X": float(coord_x_cheville_d.iloc[0]),
        "Y": float(coord_y_cheville_d.iloc[0]),
        "Z": float(coord_z_cheville_d.iloc[0]),
    }

    coord_x_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["X"]
    coord_y_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Y"]
    coord_z_cheville_g = df_frame_i[df_frame_i["Marker_Name"] == "Cheville gauche"]["Z"]
    coord_cheville_g = {
        "X": float(coord_x_cheville_g.iloc[0]),
        "Y": float(coord_y_cheville_g.iloc[0]),
        "Z": float(coord_z_cheville_g.iloc[0]),
    }

    coord_x_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["X"]
    coord_y_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Y"]
    coord_z_orteil_d = df_frame_i[df_frame_i["Marker_Name"] == "pRightToe"]["Z"]
    coord_orteil_d = {
        "X": float(coord_x_orteil_d.iloc[0]),
        "Y": float(coord_y_orteil_d.iloc[0]),
        "Z": float(coord_z_orteil_d.iloc[0]),
    }

    coord_x_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["X"]
    coord_y_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Y"]
    coord_z_orteil_g = df_frame_i[df_frame_i["Marker_Name"] == "pLeftToe"]["Z"]
    coord_orteil_g = {
        "X": float(coord_x_orteil_g.iloc[0]),
        "Y": float(coord_y_orteil_g.iloc[0]),
        "Z": float(coord_z_orteil_g.iloc[0]),
    }

    # Calcule des angles pour chaque articulation

    angle_hanche_droite = calcul_angle(coord_genou_d, coord_sternum, articulation=coord_hanche_d)
    angle_hanche_gauche = calcul_angle(coord_genou_g, coord_sternum, articulation=coord_hanche_g)

    angle_genou_droit = calcul_angle(coord_cheville_d, coord_hanche_d, articulation=coord_genou_d)
    angle_genou_gauche = calcul_angle(coord_cheville_g, coord_hanche_g, articulation=coord_genou_g)

    angle_epaule_droite = calcul_angle(coord_sternum, coord_coude_d, articulation=coord_epaule_d)
    angle_epaule_gauche = calcul_angle(coord_sternum, coord_coude_g, articulation=coord_epaule_g)

    angle_cheville_droite = calcul_angle(coord_genou_d, coord_orteil_d, articulation=coord_cheville_d)
    angle_cheville_gauche = calcul_angle(coord_genou_g, coord_orteil_g, articulation=coord_cheville_g)

    # On met à jour le dataframe avec ces angles

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche droite",
        "Angle": angle_hanche_droite,
    }

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Hanche gauche",
        "Angle": angle_hanche_gauche,
    }

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou droit",
        "Angle": angle_genou_droit,
    }

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Genou gauche",
        "Angle": angle_genou_gauche,
    }

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule droite",
        "Angle": angle_epaule_droite,
    }

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Epaule gauche",
        "Angle": angle_epaule_gauche,
    }

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville droite",
        "Angle": angle_cheville_droite,
    }

    df_angles_Route350.loc[len(df_angles_Chrono250)] = {
        "Frame": frame,
        "Articulation": "Cheville gauche",
        "Angle": angle_cheville_gauche,
    }
