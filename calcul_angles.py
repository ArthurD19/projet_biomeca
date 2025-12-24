import numpy as np
import pandas as pd

from calculer_centres_articulaires import df_centre_genou_droit_chrono250
from calculer_centres_articulaires import df_centre_genou_gauche_chrono250

from calculer_centres_articulaires import df_centre_genou_droit_chrono300
from calculer_centres_articulaires import df_centre_genou_gauche_chrono300

from calculer_centres_articulaires import df_centre_genou_droit_chrono350
from calculer_centres_articulaires import df_centre_genou_gauche_chrono350

from calculer_centres_articulaires import df_centre_genou_droit_route250
from calculer_centres_articulaires import df_centre_genou_gauche_route250

from calculer_centres_articulaires import df_centre_genou_droit_route300
from calculer_centres_articulaires import df_centre_genou_gauche_route300

from calculer_centres_articulaires import df_centre_genou_droit_route350
from calculer_centres_articulaires import df_centre_genou_gauche_route350

from calculer_centres_articulaires import df_centre_cheville_droite_chrono250
from calculer_centres_articulaires import df_centre_cheville_gauche_chrono250

from calculer_centres_articulaires import df_centre_cheville_droite_chrono300
from calculer_centres_articulaires import df_centre_cheville_gauche_chrono300

from calculer_centres_articulaires import df_centre_cheville_droite_chrono350
from calculer_centres_articulaires import df_centre_cheville_gauche_chrono350

from calculer_centres_articulaires import df_centre_cheville_droite_route250
from calculer_centres_articulaires import df_centre_cheville_gauche_route250

from calculer_centres_articulaires import df_centre_cheville_droite_route300
from calculer_centres_articulaires import df_centre_cheville_gauche_route300

from calculer_centres_articulaires import df_centre_cheville_droite_route350
from calculer_centres_articulaires import df_centre_cheville_gauche_route350

# Lecture des fichiers CSV

df_Chrono250 = pd.read_csv("Chrono250.csv")
df_Chrono300 = pd.read_csv("Chrono300.csv")
df_Chrono350 = pd.read_csv("Chrono350.csv")
df_Route250 = pd.read_csv("Route250.csv")
df_Route300 = pd.read_csv("Route300.csv")
df_Route350 = pd.read_csv("Route350.csv")

# FONCTION UTILES #


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

# On commence par faire le dataframe permettant de calculer les angles du genou

# Chrono250

df_genou_droit_chrono250 = (
    pd.concat([df_Chrono250, df_centre_genou_droit_chrono250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_genou_gauche_chrono250 = (
    pd.concat([df_Chrono250, df_centre_genou_gauche_chrono250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Chrono300

df_genou_droit_chrono300 = (
    pd.concat([df_Chrono300, df_centre_genou_droit_chrono300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_genou_gauche_chrono300 = (
    pd.concat([df_Chrono300, df_centre_genou_gauche_chrono300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Chrono350

df_genou_droit_chrono350 = (
    pd.concat([df_Chrono350, df_centre_genou_droit_chrono350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_genou_gauche_chrono350 = (
    pd.concat([df_Chrono350, df_centre_genou_gauche_chrono350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Route250

df_genou_droit_route250 = (
    pd.concat([df_Route250, df_centre_genou_droit_route250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_genou_gauche_route250 = (
    pd.concat([df_Route250, df_centre_genou_gauche_route250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Route300

df_genou_droit_route300 = (
    pd.concat([df_Route300, df_centre_genou_droit_route300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_genou_gauche_route300 = (
    pd.concat([df_Route300, df_centre_genou_gauche_route300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Route350

df_genou_droit_route350 = (
    pd.concat([df_Route350, df_centre_genou_droit_route350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_genou_gauche_route350 = (
    pd.concat([df_Route350, df_centre_genou_gauche_route350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

##################################################################################################

# Maintenant, on fait le dataframe pour le calcul des angles de la cheville

# Chrono250

df_cheville_droite_chrono250 = (
    pd.concat([df_Chrono250, df_centre_cheville_droite_chrono250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_cheville_gauche_chrono250 = (
    pd.concat([df_Chrono250, df_centre_cheville_gauche_chrono250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Chrono300

df_cheville_droite_chrono300 = (
    pd.concat([df_Chrono300, df_centre_cheville_droite_chrono300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_cheville_gauche_chrono300 = (
    pd.concat([df_Chrono300, df_centre_cheville_gauche_chrono300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Chrono350

df_cheville_droite_chrono350 = (
    pd.concat([df_Chrono350, df_centre_cheville_droite_chrono350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_cheville_gauche_chrono350 = (
    pd.concat([df_Chrono350, df_centre_cheville_gauche_chrono350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Route250

df_cheville_droite_route250 = (
    pd.concat([df_Route250, df_centre_cheville_droite_route250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_cheville_gauche_route250 = (
    pd.concat([df_Route250, df_centre_cheville_gauche_route250], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Route300

df_cheville_droite_route300 = (
    pd.concat([df_Route300, df_centre_cheville_droite_route300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_cheville_gauche_route300 = (
    pd.concat([df_Route300, df_centre_cheville_gauche_route300], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

# Route350

df_cheville_droite_route350 = (
    pd.concat([df_Route350, df_centre_cheville_droite_route350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)

df_cheville_gauche_route350 = (
    pd.concat([df_Route350, df_centre_cheville_gauche_route350], ignore_index=True)
    .sort_values(by="Frame")
    .reset_index(drop=True)
)
