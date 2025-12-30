import pandas as pd
import numpy as np


#####################################################################################################

# Lecture des fichiers CSV

df_Chrono250 = pd.read_csv("Chrono250.csv")
df_Chrono300 = pd.read_csv("Chrono300.csv")
df_Chrono350 = pd.read_csv("Chrono350.csv")
df_Route250 = pd.read_csv("Route250.csv")
df_Route300 = pd.read_csv("Route300.csv")
df_Route350 = pd.read_csv("Route350.csv")

# Liste des variables utiles
liste_noms_points_utiles = [
    "pPX",
    "pRightASI",
    "pLeftASI",
    "pRightCSI",
    "pLeftCSI",
    "pRightKneeLatEpicondyle",
    "pRightKneeMedEpicondyle",
    "pLeftKneeLatEpicondyle",
    "pLeftKneeMedEpicondyle",
    "pLeftMedMalleolus",
    "pLeftLatMalleolus",
    "pRightMedMalleolus",
    "pRightLatMalleolus",
    "pRightToe",
    "pLeftToe",
    "pRightArmLatEpicondyle",
    "pRightArmMedEpicondyle",
    "pLeftArmLatEpicondyle",
    "pLeftArmMedEpicondyle",
    "pRightAcromion",
    "pLeftAcromion"
]

# On ne garde que les colonnes utiles pour chaque tableau
df_Chrono250 = df_Chrono250[df_Chrono250["Marker_Name"].isin(liste_noms_points_utiles)]
df_Chrono300 = df_Chrono300[df_Chrono300["Marker_Name"].isin(liste_noms_points_utiles)]
df_Chrono350 = df_Chrono350[df_Chrono350["Marker_Name"].isin(liste_noms_points_utiles)]
df_Route250 = df_Route250[df_Route250["Marker_Name"].isin(liste_noms_points_utiles)]
df_Route300 = df_Route300[df_Route300["Marker_Name"].isin(liste_noms_points_utiles)]
df_Route350 = df_Route350[df_Route350["Marker_Name"].isin(liste_noms_points_utiles)]

# Liste des variables utiles par articulation
utiles_cheville_droite = ["pRightMedMalleolus", "pRightLatMalleolus"]
utiles_cheville_gauche = ["pLeftMedMalleolus", "pLeftLatMalleolus"]
utiles_coude_droit = ["pRightArmLatEpicondyle", "pRightArmMedEpicondyle"]
utiles_coude_gauche = ["pLeftArmLatEpicondyle", "pLeftArmMedEpicondyle"]
utiles_genou_droit = ["pRightKneeLatEpicondyle", "pRightKneeMedEpicondyle"]
utiles_genou_gauche = ["pLeftKneeLatEpicondyle", "pLeftKneeMedEpicondyle"]
utiles_pelvis = ["pRightASI", "pLeftASI"]
utiles_d_w = ["pRightASI", "pLeftASI", "pRightCSI", "pLeftCSI"]

##################################################################################################

# On initialise les tableaux des centres articulaires 

centre_Chrono250 = []
centre_Chrono300 = []
centre_Chrono350 = []
centre_Route250 = []
centre_Route300 = []
centre_Route350 = []

##################################################################################################

# Calcul pour le pelvis -Chrono250

for frame in df_Chrono250["Frame"].unique():
    df_droite = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_pelvis)) &
                             (df_Chrono250["Frame"] == frame)]
    # Calcul du centre
    coord_X = df_droite["X"].mean()
    coord_Y = df_droite["Y"].mean()
    coord_Z = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Pelvis",
         "X": coord_X,
         "Y": coord_Y,
         "Z": coord_Z}
    )

# Calcul pour le pelvis -Chrono300

for frame in df_Chrono300["Frame"].unique():
    df_droite = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_pelvis)) &
                             (df_Chrono300["Frame"] == frame)]
    # Calcul du centre
    coord_X = df_droite["X"].mean()
    coord_Y = df_droite["Y"].mean()
    coord_Z = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Pelvis",
         "X": coord_X,
         "Y": coord_Y,
         "Z": coord_Z}
    )

# Calcul pour le pelvis -Chrono350

for frame in df_Chrono350["Frame"].unique():
    df_droite = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_pelvis)) &
                             (df_Chrono350["Frame"] == frame)]
    # Calcul du centre
    coord_X = df_droite["X"].mean()
    coord_Y = df_droite["Y"].mean()
    coord_Z = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Pelvis",
         "X": coord_X,
         "Y": coord_Y,
         "Z": coord_Z}
    )

# Calcul pour le pelvis -Route250

for frame in df_Route250["Frame"].unique():
    df_droite = df_Route250[(df_Route250["Marker_Name"].isin(utiles_pelvis)) &
                            (df_Route250["Frame"] == frame)]
    # Calcul du centre
    coord_X = df_droite["X"].mean()
    coord_Y = df_droite["Y"].mean()
    coord_Z = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Pelvis",
         "X": coord_X,
         "Y": coord_Y,
         "Z": coord_Z}
    )

# Calcul pour le pelvis -Route300

for frame in df_Route300["Frame"].unique():
    df_droite = df_Route300[(df_Route300["Marker_Name"].isin(utiles_pelvis)) &
                            (df_Route300["Frame"] == frame)]
    # Calcul du centre
    coord_X = df_droite["X"].mean()
    coord_Y = df_droite["Y"].mean()
    coord_Z = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Pelvis",
         "X": coord_X,
         "Y": coord_Y,
         "Z": coord_Z}
    )

# Calcul pour le pelvis -Route350

for frame in df_Route350["Frame"].unique():
    df_droite = df_Route350[(df_Route350["Marker_Name"].isin(utiles_pelvis)) &
                            (df_Route350["Frame"] == frame)]
    # Calcul du centre
    coord_X = df_droite["X"].mean()
    coord_Y = df_droite["Y"].mean()
    coord_Z = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Pelvis",
         "X": coord_X,
         "Y": coord_Y,
         "Z": coord_Z}
    )

######################################################################################################

# Calcul du centre articulaire de la cheville - Chrono250

for frame in df_Chrono250["Frame"].unique():
    df_droite = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_cheville_droite)) &
                             (df_Chrono250["Frame"] == frame)]
    df_gauche = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_cheville_gauche)) &
                             (df_Chrono250["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Cheville droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Cheville gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire de la cheville - Chrono300

for frame in df_Chrono300["Frame"].unique():
    df_droite = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_cheville_droite)) &
                             (df_Chrono300["Frame"] == frame)]
    df_gauche = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_cheville_gauche)) &
                             (df_Chrono300["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Cheville droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Cheville gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire de la cheville - Chrono350

for frame in df_Chrono350["Frame"].unique():
    df_droite = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_cheville_droite)) &
                             (df_Chrono350["Frame"] == frame)]
    df_gauche = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_cheville_gauche)) &
                             (df_Chrono350["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Cheville droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Cheville gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire de la cheville - Route250

for frame in df_Route250["Frame"].unique():
    df_droite = df_Route250[(df_Route250["Marker_Name"].isin(utiles_cheville_droite)) &
                            (df_Route250["Frame"] == frame)]
    df_gauche = df_Route250[(df_Route250["Marker_Name"].isin(utiles_cheville_gauche)) &
                            (df_Route250["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Cheville droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Cheville gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire de la cheville - Route300

for frame in df_Route300["Frame"].unique():
    df_droite = df_Route300[(df_Route300["Marker_Name"].isin(utiles_cheville_droite)) &
                            (df_Route300["Frame"] == frame)]
    df_gauche = df_Route300[(df_Route300["Marker_Name"].isin(utiles_cheville_gauche)) &
                            (df_Route300["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Cheville droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Cheville gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire de la cheville - Chrono350

for frame in df_Route350["Frame"].unique():
    df_droite = df_Route350[(df_Route350["Marker_Name"].isin(utiles_cheville_droite)) &
                            (df_Route350["Frame"] == frame)]
    df_gauche = df_Route350[(df_Route350["Marker_Name"].isin(utiles_cheville_gauche)) &
                            (df_Route350["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Cheville droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre de cheville droite
    centre_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Cheville gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

###################################################################################################

# Calcul du centre articulaire du genou - Chrono250

for frame in df_Chrono250["Frame"].unique():
    df_droite = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_genou_droit)) &
                             (df_Chrono250["Frame"] == frame)]
    df_gauche = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_genou_gauche)) &
                             (df_Chrono250["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du genou droit
    centre_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Genou droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du genou gauche
    centre_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Genou gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du genou - Chrono300

for frame in df_Chrono300["Frame"].unique():
    df_droite = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_genou_droit)) &
                             (df_Chrono300["Frame"] == frame)]
    df_gauche = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_genou_gauche)) &
                             (df_Chrono300["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du genou droit
    centre_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Genou droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du genou gauche
    centre_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Genou gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du genou - Chrono350

for frame in df_Chrono350["Frame"].unique():
    df_droite = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_genou_droit)) &
                             (df_Chrono350["Frame"] == frame)]
    df_gauche = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_genou_gauche)) &
                             (df_Chrono350["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du genou droit
    centre_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Genou droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du genou gauche
    centre_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Genou gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du genou - Route250

for frame in df_Route250["Frame"].unique():
    df_droite = df_Route250[(df_Route250["Marker_Name"].isin(utiles_genou_droit)) &
                            (df_Route250["Frame"] == frame)]
    df_gauche = df_Route250[(df_Route250["Marker_Name"].isin(utiles_genou_gauche)) &
                            (df_Route250["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du genou droit
    centre_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Genou droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du genou gauche
    centre_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Genou gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg})

# Calcul du centre articulaire du genou - Route300

for frame in df_Route300["Frame"].unique():
    df_droite = df_Route300[(df_Route300["Marker_Name"].isin(utiles_genou_droit)) &
                            (df_Route300["Frame"] == frame)]
    df_gauche = df_Route300[(df_Route300["Marker_Name"].isin(utiles_genou_gauche)) &
                            (df_Route300["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du genou droit
    centre_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Genou droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du genou gauche
    centre_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Genou gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du genou - Route350

for frame in df_Route350["Frame"].unique():
    df_droite = df_Route350[(df_Route350["Marker_Name"].isin(utiles_genou_droit)) &
                            (df_Route350["Frame"] == frame)]
    df_gauche = df_Route350[(df_Route350["Marker_Name"].isin(utiles_genou_gauche)) &
                            (df_Route350["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du genou droit
    centre_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Genou droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du genou gauche
    centre_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Genou gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

###############################################################################################

# Calcul du centre articulaire du coude - Chrono250

for frame in df_Chrono250["Frame"].unique():
    df_droite = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_coude_droit)) &
                             (df_Chrono250["Frame"] == frame)]
    df_gauche = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_coude_gauche)) &
                             (df_Chrono250["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du coude droit
    centre_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Coude droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du coude gauche
    centre_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Coude gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du coude - Chrono300

for frame in df_Chrono300["Frame"].unique():
    df_droite = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_coude_droit)) &
                             (df_Chrono300["Frame"] == frame)]
    df_gauche = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_coude_gauche)) &
                             (df_Chrono300["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du coude droit
    centre_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Coude droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du coude gauche
    centre_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Coude gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du coude - Chrono350

for frame in df_Chrono350["Frame"].unique():
    df_droite = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_coude_droit)) &
                             (df_Chrono350["Frame"] == frame)]
    df_gauche = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_coude_gauche)) &
                             (df_Chrono350["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du coude droit
    centre_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Coude droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du coude gauche
    centre_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Coude gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du coude - Route250

for frame in df_Route250["Frame"].unique():
    df_droite = df_Route250[(df_Route250["Marker_Name"].isin(utiles_coude_droit)) &
                            (df_Route250["Frame"] == frame)]
    df_gauche = df_Route250[(df_Route250["Marker_Name"].isin(utiles_coude_gauche)) &
                            (df_Route250["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du coude droit
    centre_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Coude droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du coude gauche
    centre_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Coude gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg})

# Calcul du centre articulaire du coude - Route300

for frame in df_Route300["Frame"].unique():
    df_droite = df_Route300[(df_Route300["Marker_Name"].isin(utiles_coude_droit)) &
                            (df_Route300["Frame"] == frame)]
    df_gauche = df_Route300[(df_Route300["Marker_Name"].isin(utiles_coude_gauche)) &
                            (df_Route300["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du coude droit
    centre_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Coude droit",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du coude gauche
    centre_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Coude gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

# Calcul du centre articulaire du coude - Route350

for frame in df_Route350["Frame"].unique():
    df_droite = df_Route350[(df_Route350["Marker_Name"].isin(utiles_coude_droit)) &
                            (df_Route350["Frame"] == frame)]
    df_gauche = df_Route350[(df_Route350["Marker_Name"].isin(utiles_coude_gauche)) &
                            (df_Route350["Frame"] == frame)]
    # Calcul du centre articulaire (droite)
    coord_Xd = df_droite["X"].mean()
    coord_Yd = df_droite["Y"].mean()
    coord_Zd = df_droite["Z"].mean()
    # On l'ajoute au centre du coude droit
    centre_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Coude droite",
         "X": coord_Xd,
         "Y": coord_Yd,
         "Z": coord_Zd}
    )
    # Calcul du centre articulaire (gauche)
    coord_Xg = df_gauche["X"].mean()
    coord_Yg = df_gauche["Y"].mean()
    coord_Zg = df_gauche["Z"].mean()
    # On l'ajoute au centre du coude gauche
    centre_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Coude gauche",
         "X": coord_Xg,
         "Y": coord_Yg,
         "Z": coord_Zg}
    )

###############################################################################################

# Calcul de d et w - Chrono250
w_Chrono250 = []
d_Chrono250 = []

for frame in df_Chrono250["Frame"].unique():
    df_droite = df_Chrono250[(df_Chrono250["Marker_Name"].isin(utiles_d_w)) &
                             (df_Chrono250["Frame"] == frame)]
    # Calcul de w
    w = df_droite[df_droite["Marker_Name"] == "pRightASI"] - df_droite[df_droite["Marker_Name"] == "pLeftASI"]
    # Calcul de d
    centre_1_x = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["X"].values[0])) / 2
    centre_1_y = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Y"].values[0])) / 2
    centre_1_z = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Z"].values[0])) / 2
    centre_2_x = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["X"].values[0])) / 2
    centre_2_y = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Y"].values[0])) / 2
    centre_2_z = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Z"].values[0])) / 2
    d = np.sqrt(
        (centre_1_x - centre_2_x)**2 + (centre_1_y - centre_2_y)**2 + (centre_1_z - centre_2_z)**2
    )
    # On les ajoute à w et à d
    w_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "W",
         "W": w}
    )
    d_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "D",
         "D": d}
    )

# Calcul de d et w - Chrono300
w_Chrono300 = []
d_Chrono300 = []

for frame in df_Chrono300["Frame"].unique():
    df_droite = df_Chrono300[(df_Chrono300["Marker_Name"].isin(utiles_d_w)) &
                             (df_Chrono300["Frame"] == frame)]
    # Calcul de w
    w = df_droite[df_droite["Marker_Name"] == "pRightASI"] - df_droite[df_droite["Marker_Name"] == "pLeftASI"]
    # Calcul de d
    centre_1_x = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["X"].values[0])) / 2
    centre_1_y = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Y"].values[0])) / 2
    centre_1_z = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Z"].values[0])) / 2
    centre_2_x = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["X"].values[0])) / 2
    centre_2_y = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Y"].values[0])) / 2
    centre_2_z = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Z"].values[0])) / 2
    d = np.sqrt(
        (centre_1_x - centre_2_x)**2 + (centre_1_y - centre_2_y)**2 + (centre_1_z - centre_2_z)**2
    )
    # On les ajoute à w et à d
    w_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "W",
         "W": w}
    )
    d_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "D",
         "D": d}
    )

# Calcul de d et w - Chrono350
w_Chrono350 = []
d_Chrono350 = []

for frame in df_Chrono350["Frame"].unique():
    df_droite = df_Chrono350[(df_Chrono350["Marker_Name"].isin(utiles_d_w)) &
                             (df_Chrono350["Frame"] == frame)]
    # Calcul de w
    w = df_droite[df_droite["Marker_Name"] == "pRightASI"] - df_droite[df_droite["Marker_Name"] == "pLeftASI"]
    # Calcul de d
    centre_1_x = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["X"].values[0])) / 2
    centre_1_y = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Y"].values[0])) / 2
    centre_1_z = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Z"].values[0])) / 2
    centre_2_x = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["X"].values[0])) / 2
    centre_2_y = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Y"].values[0])) / 2
    centre_2_z = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Z"].values[0])) / 2
    d = np.sqrt(
        (centre_1_x - centre_2_x)**2 + (centre_1_y - centre_2_y)**2 + (centre_1_z - centre_2_z)**2
    )
    # On les ajoute à w et à d
    w_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "W",
         "W": w}
    )
    d_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "D",
         "D": d}
    )

# Calcul de d et w - Route250
w_Route250 = []
d_Route250 = []

for frame in df_Route250["Frame"].unique():
    df_droite = df_Route250[(df_Route250["Marker_Name"].isin(utiles_d_w)) &
                            (df_Route250["Frame"] == frame)]
    # Calcul de w
    w = df_droite[df_droite["Marker_Name"] == "pRightASI"] - df_droite[df_droite["Marker_Name"] == "pLeftASI"]
    # Calcul de d
    centre_1_x = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["X"].values[0])) / 2
    centre_1_y = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Y"].values[0])) / 2
    centre_1_z = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Z"].values[0])) / 2
    centre_2_x = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["X"].values[0])) / 2
    centre_2_y = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Y"].values[0])) / 2
    centre_2_z = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Z"].values[0])) / 2
    d = np.sqrt(
        (centre_1_x - centre_2_x)**2 + (centre_1_y - centre_2_y)**2 + (centre_1_z - centre_2_z)**2
    )
    # On les ajoute à w et à d
    w_Route250.append({"Frame": frame, "Marker_Name": "W", "W": w})
    d_Route250.append({"Frame": frame, "Marker_Name": "D", "D": d})

# Calcul de d et w - Route300
w_Route300 = []
d_Route300 = []

for frame in df_Route300["Frame"].unique():
    df_droite = df_Route300[(df_Route300["Marker_Name"].isin(utiles_d_w)) &
                            (df_Route300["Frame"] == frame)]
    # Calcul de w
    w = df_droite[df_droite["Marker_Name"] == "pRightASI"] - df_droite[df_droite["Marker_Name"] == "pLeftASI"]
    # Calcul de d
    centre_1_x = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["X"].values[0])) / 2
    centre_1_y = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Y"].values[0])) / 2
    centre_1_z = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Z"].values[0])) / 2
    centre_2_x = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["X"].values[0])) / 2
    centre_2_y = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Y"].values[0])) / 2
    centre_2_z = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Z"].values[0])) / 2
    d = np.sqrt(
        (centre_1_x - centre_2_x)**2 + (centre_1_y - centre_2_y)**2 + (centre_1_z - centre_2_z)**2
    )
    # On les ajoute à w et à d
    w_Route300.append({"Frame": frame, "Marker_Name": "W", "W": w})
    d_Route300.append({"Frame": frame, "Marker_Name": "D", "D": d})

# Calcul de d et w - Route350
w_Route350 = []
d_Route350 = []

for frame in df_Route350["Frame"].unique():
    df_droite = df_Route350[(df_Route350["Marker_Name"].isin(utiles_d_w)) &
                            (df_Route350["Frame"] == frame)]
    # Calcul de w
    w = df_droite[df_droite["Marker_Name"] == "pRightASI"] - df_droite[df_droite["Marker_Name"] == "pLeftASI"]
    # Calcul de d
    centre_1_x = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["X"].values[0])) / 2
    centre_1_y = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Y"].values[0])) / 2
    centre_1_z = ((df_droite[df_droite["Marker_Name"] == "pRightASI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftASI"]["Z"].values[0])) / 2
    centre_2_x = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["X"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["X"].values[0])) / 2
    centre_2_y = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Y"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Y"].values[0])) / 2
    centre_2_z = ((df_droite[df_droite["Marker_Name"] == "pRightCSI"]["Z"].values[0]) +
                  (df_droite[df_droite["Marker_Name"] == "pLeftCSI"]["Z"].values[0])) / 2
    d = np.sqrt(
        (centre_1_x - centre_2_x)**2 + (centre_1_y - centre_2_y)**2 + (centre_1_z - centre_2_z)**2
    )
    # On les ajoute à w et à d
    w_Route350.append({"Frame": frame, "Marker_Name": "W", "W": w})
    d_Route350.append({"Frame": frame, "Marker_Name": "D", "D": d})

# On convertit les w et d en dataframe
df_w_Chrono250 = pd.DataFrame(w_Chrono250)
df_w_Chrono300 = pd.DataFrame(w_Chrono300)
df_w_Chrono350 = pd.DataFrame(w_Chrono350)
df_w_Route250 = pd.DataFrame(w_Route250)
df_w_Route300 = pd.DataFrame(w_Route300)
df_w_Route350 = pd.DataFrame(w_Route350)
df_d_Chrono250 = pd.DataFrame(d_Chrono250)
df_d_Chrono300 = pd.DataFrame(d_Chrono300)
df_d_Chrono350 = pd.DataFrame(d_Chrono350)
df_d_Route250 = pd.DataFrame(d_Route250)
df_d_Route300 = pd.DataFrame(d_Route300)
df_d_Route350 = pd.DataFrame(d_Route350)

################################################################################################

# On convertit les listes en dataframe

df_Chrono250 = pd.DataFrame(centre_Chrono250)
df_Chrono300 = pd.DataFrame(centre_Chrono300)
df_Chrono350 = pd.DataFrame(centre_Chrono350)
df_Route250 = pd.DataFrame(centre_Route250)
df_Route300 = pd.DataFrame(centre_Route300)
df_Route350 = pd.DataFrame(centre_Route350)

################################################################################################

# Calcul centre hanche - Chrono250
centre_hanche_droit_Chrono250 = []
centre_hanche_gauche_Chrono250 = []

for frame in df_Chrono250["Frame"].unique():
    df_centre_pelvis_frame = df_Chrono250[df_Chrono250["Frame"] == frame &
                                          df_Chrono250["Marker_Name"] == "Pelvis"]
    df_d_Chrono250_frame = df_d_Chrono250[df_d_Chrono250["Frame"] == frame]
    df_w_Chrono250_frame = df_w_Chrono250[df_w_Chrono250["Frame"] == frame]

    coord_X_gauche = df_centre_pelvis_frame["X"].values[0] - 0.3 * df_d_Chrono250_frame["D"].values[0]
    coord_X_droit = coord_X_gauche

    coord_Z_gauche = df_centre_pelvis_frame["Z"].values[0] - 0.35 * df_w_Chrono250_frame["W"].values[0]
    coord_Z_droit = coord_Z_gauche

    coord_Y_gauche = df_centre_pelvis_frame["Y"].values[0] + 0.19 * df_w_Chrono250_frame["W"].values[0]
    coord_Y_droit = df_centre_pelvis_frame["Y"].values[0] - 0.19 * df_w_Chrono250_frame["W"].values[0]

    centre_hanche_gauche_Chrono250.append(
        {
            "Frame": frame,
            "Marker_Name": "Hanche gauche",
            "X": coord_X_gauche,
            "Y": coord_Y_gauche,
            "Z": coord_Z_gauche,
        }
    )
    centre_hanche_droit_Chrono250.append(
        {"Frame": frame,
         "Marker_Name": "Hanche droite",
         "X": coord_X_droit,
         "Y": coord_Y_droit,
         "Z": coord_Z_droit})

# Calcul centre hanche - Chrono300
centre_hanche_droit_Chrono300 = []
centre_hanche_gauche_Chrono300 = []

for frame in df_Chrono300["Frame"].unique():
    df_centre_pelvis_frame = df_Chrono300[df_Chrono300["Frame"] == frame &
                                          df_Chrono300["Marker_Name"] == "Pelvis"]
    df_d_Chrono300_frame = df_d_Chrono300[df_d_Chrono300["Frame"] == frame]
    df_w_Chrono300_frame = df_w_Chrono300[df_w_Chrono300["Frame"] == frame]

    coord_X_gauche = df_centre_pelvis_frame["X"].values[0] - 0.3 * df_d_Chrono300_frame["D"].values[0]
    coord_X_droit = coord_X_gauche

    coord_Z_gauche = df_centre_pelvis_frame["Z"].values[0] - 0.35 * df_w_Chrono300_frame["W"].values[0]
    coord_Z_droit = coord_Z_gauche

    coord_Y_gauche = df_centre_pelvis_frame["Y"].values[0] + 0.19 * df_w_Chrono300_frame["W"].values[0]
    coord_Y_droit = df_centre_pelvis_frame["Y"].values[0] - 0.19 * df_w_Chrono300_frame["W"].values[0]

    centre_hanche_gauche_Chrono300.append(
        {
            "Frame": frame,
            "Marker_Name": "Hanche gauche",
            "X": coord_X_gauche,
            "Y": coord_Y_gauche,
            "Z": coord_Z_gauche,
        }
    )
    centre_hanche_droit_Chrono300.append(
        {"Frame": frame,
         "Marker_Name": "Hanche droite",
         "X": coord_X_droit,
         "Y": coord_Y_droit,
         "Z": coord_Z_droit})

# Calcul centre hanche - Chrono350
centre_hanche_droit_Chrono350 = []
centre_hanche_gauche_Chrono350 = []

for frame in df_Chrono350["Frame"].unique():
    df_centre_pelvis_frame = df_Chrono350[df_Chrono350["Frame"] == frame &
                                          df_Chrono350["Marker_Name"] == "Pelvis"]
    df_d_Chrono350_frame = df_d_Chrono350[df_d_Chrono350["Frame"] == frame]
    df_w_Chrono350_frame = df_w_Chrono350[df_w_Chrono350["Frame"] == frame]

    coord_X_gauche = df_centre_pelvis_frame["X"].values[0] - 0.3 * df_d_Chrono350_frame["D"].values[0]
    coord_X_droit = coord_X_gauche

    coord_Z_gauche = df_centre_pelvis_frame["Z"].values[0] - 0.35 * df_w_Chrono350_frame["W"].values[0]
    coord_Z_droit = coord_Z_gauche

    coord_Y_gauche = df_centre_pelvis_frame["Y"].values[0] + 0.19 * df_w_Chrono350_frame["W"].values[0]
    coord_Y_droit = df_centre_pelvis_frame["Y"].values[0] - 0.19 * df_w_Chrono350_frame["W"].values[0]

    centre_hanche_gauche_Chrono350.append(
        {
            "Frame": frame,
            "Marker_Name": "Hanche gauche",
            "X": coord_X_gauche,
            "Y": coord_Y_gauche,
            "Z": coord_Z_gauche,
        }
    )
    centre_hanche_droit_Chrono350.append(
        {"Frame": frame,
         "Marker_Name": "Hanche droite",
         "X": coord_X_droit,
         "Y": coord_Y_droit,
         "Z": coord_Z_droit})

# Calcul centre hanche - Route250
centre_hanche_droit_Route250 = []
centre_hanche_gauche_Route250 = []

for frame in df_Route250["Frame"].unique():
    df_centre_pelvis_frame = df_Route250[df_Route250["Frame"] == frame &
                                         df_Route250["Marker_Name"] == "Pelvis"]
    df_d_Route250_frame = df_d_Route250[df_d_Route250["Frame"] == frame]
    df_w_Route250_frame = df_w_Route250[df_w_Route250["Frame"] == frame]

    coord_X_gauche = df_centre_pelvis_frame["X"].values[0] - 0.3 * df_d_Route250_frame["D"].values[0]
    coord_X_droit = coord_X_gauche

    coord_Z_gauche = df_centre_pelvis_frame["Z"].values[0] - 0.35 * df_w_Route250_frame["W"].values[0]
    coord_Z_droit = coord_Z_gauche

    coord_Y_gauche = df_centre_pelvis_frame["Y"].values[0] + 0.19 * df_w_Route250_frame["W"].values[0]
    coord_Y_droit = df_centre_pelvis_frame["Y"].values[0] - 0.19 * df_w_Route250_frame["W"].values[0]

    centre_hanche_gauche_Route250.append(
        {
            "Frame": frame,
            "Marker_Name": "Hanche gauche",
            "X": coord_X_gauche,
            "Y": coord_Y_gauche,
            "Z": coord_Z_gauche,
        }
    )
    centre_hanche_droit_Route250.append(
        {"Frame": frame,
         "Marker_Name": "Hanche droite",
         "X": coord_X_droit,
         "Y": coord_Y_droit,
         "Z": coord_Z_droit})

# Calcul centre hanche - Route300
centre_hanche_droit_Route300 = []
centre_hanche_gauche_Route300 = []

for frame in df_Route300["Frame"].unique():
    df_centre_pelvis_frame = df_Route300[df_Route300["Frame"] == frame &
                                         df_Route300["Marker_Name"] == "Pelvis"]
    df_d_Route300_frame = df_d_Route300[df_d_Route300["Frame"] == frame]
    df_w_Route300_frame = df_w_Route300[df_w_Route300["Frame"] == frame]

    coord_X_gauche = df_centre_pelvis_frame["X"].values[0] - 0.3 * df_d_Route300_frame["D"].values[0]
    coord_X_droit = coord_X_gauche

    coord_Z_gauche = df_centre_pelvis_frame["Z"].values[0] - 0.35 * df_w_Route300_frame["W"].values[0]
    coord_Z_droit = coord_Z_gauche

    coord_Y_gauche = df_centre_pelvis_frame["Y"].values[0] + 0.19 * df_w_Route300_frame["W"].values[0]
    coord_Y_droit = df_centre_pelvis_frame["Y"].values[0] - 0.19 * df_w_Route300_frame["W"].values[0]

    centre_hanche_gauche_Route300.append(
        {
            "Frame": frame,
            "Marker_Name": "Hanche gauche",
            "X": coord_X_gauche,
            "Y": coord_Y_gauche,
            "Z": coord_Z_gauche,
        }
    )
    centre_hanche_droit_Route300.append(
        {"Frame": frame,
         "Marker_Name": "Hanche droite",
         "X": coord_X_droit,
         "Y": coord_Y_droit,
         "Z": coord_Z_droit})

# Calcul centre hanche - Route350
centre_hanche_droit_Route350 = []
centre_hanche_gauche_Route350 = []

for frame in df_Route350["Frame"].unique():
    df_centre_pelvis_frame = df_Route350[df_Route350["Frame"] == frame &
                                         df_Route350["Marker_Name"] == "Pelvis"]
    df_d_Route350_frame = df_d_Route350[df_d_Route350["Frame"] == frame]
    df_w_Route350_frame = df_w_Route350[df_w_Route350["Frame"] == frame]

    coord_X_gauche = df_centre_pelvis_frame["X"].values[0] - 0.3 * df_d_Route350_frame["D"].values[0]
    coord_X_droit = coord_X_gauche

    coord_Z_gauche = df_centre_pelvis_frame["Z"].values[0] - 0.35 * df_w_Route350_frame["W"].values[0]
    coord_Z_droit = coord_Z_gauche

    coord_Y_gauche = df_centre_pelvis_frame["Y"].values[0] + 0.19 * df_w_Route350_frame["W"].values[0]
    coord_Y_droit = df_centre_pelvis_frame["Y"].values[0] - 0.19 * df_w_Route350_frame["W"].values[0]

    centre_hanche_gauche_Route350.append(
        {
            "Frame": frame,
            "Marker_Name": "Hanche gauche",
            "X": coord_X_gauche,
            "Y": coord_Y_gauche,
            "Z": coord_Z_gauche,
        }
    )
    centre_hanche_droit_Route350.append(
        {"Frame": frame,
         "Marker_Name": "Hanche droite",
         "X": coord_X_droit,
         "Y": coord_Y_droit,
         "Z": coord_Z_droit})

# On les concertit en dataframe
df_centre_hanche_droite_chrono250 = pd.DataFrame(centre_hanche_droit_Chrono250)
df_centre_hanche_gauche_chrono250 = pd.DataFrame(centre_hanche_gauche_Chrono250)
df_centre_hanche_droite_chrono300 = pd.DataFrame(centre_hanche_droit_Chrono300)
df_centre_hanche_gauche_chrono300 = pd.DataFrame(centre_hanche_gauche_Chrono300)
df_centre_hanche_droite_chrono350 = pd.DataFrame(centre_hanche_droit_Chrono350)
df_centre_hanche_gauche_chrono350 = pd.DataFrame(centre_hanche_gauche_Chrono350)
df_centre_hanche_droite_route250 = pd.DataFrame(centre_hanche_droit_Route250)
df_centre_hanche_gauche_route250 = pd.DataFrame(centre_hanche_gauche_Route250)
df_centre_hanche_droite_route300 = pd.DataFrame(centre_hanche_droit_Route300)
df_centre_hanche_gauche_route300 = pd.DataFrame(centre_hanche_gauche_Route300)
df_centre_hanche_droite_route350 = pd.DataFrame(centre_hanche_droit_Route350)
df_centre_hanche_gauche_route350 = pd.DataFrame(centre_hanche_gauche_Route350)

#######################################################################################

# On concatène les tableaux ainsi obtenus avec les tableaux précédents

df_chrono250 = (
    pd.concat([df_Chrono250, df_centre_hanche_gauche_chrono250, df_centre_hanche_droite_chrono250],
              ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_chrono300 = (
    pd.concat([df_Chrono300, df_centre_hanche_gauche_chrono300, df_centre_hanche_droite_chrono300],
              ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_chrono350 = (
    pd.concat([df_Chrono350, df_centre_hanche_gauche_chrono350, df_centre_hanche_droite_chrono350],
              ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_route250 = (
    pd.concat([df_Route250, df_centre_hanche_gauche_route250, df_centre_hanche_droite_route250],
              ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_route300 = (
    pd.concat([df_Route300, df_centre_hanche_gauche_route300, df_centre_hanche_droite_route300],
              ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_route350 = (
    pd.concat([df_Route350, df_centre_hanche_gauche_route350, df_centre_hanche_droite_route350],
              ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)
