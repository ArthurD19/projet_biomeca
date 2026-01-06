import pandas as pd
import numpy as np

from calcul_vitesses import df_cheville_droite_Chrono250, df_cheville_gauche_Chrono250, df_epaule_droite_Chrono250, df_epaule_gauche_Chrono250, df_genou_droit_Chrono250, df_genou_gauche_Chrono250, df_hanche_droite_Chrono250, df_hanche_gauche_Chrono250
from calcul_vitesses import df_cheville_droite_Chrono300, df_cheville_gauche_Chrono300, df_epaule_droite_Chrono300, df_epaule_gauche_Chrono300, df_genou_droit_Chrono300, df_genou_gauche_Chrono300, df_hanche_droite_Chrono300, df_hanche_gauche_Chrono300
from calcul_vitesses import df_cheville_droite_Chrono350, df_cheville_gauche_Chrono350, df_epaule_droite_Chrono350, df_epaule_gauche_Chrono350, df_genou_droit_Chrono350, df_genou_gauche_Chrono350, df_hanche_droite_Chrono350, df_hanche_gauche_Chrono350
from calcul_vitesses import df_cheville_droite_Route250, df_cheville_gauche_Route250, df_epaule_droite_Route250, df_epaule_gauche_Route250, df_genou_droit_Route250, df_genou_gauche_Route250, df_hanche_droite_Route250, df_hanche_gauche_Route250
from calcul_vitesses import df_cheville_droite_Route300, df_cheville_gauche_Route300, df_epaule_droite_Route300, df_epaule_gauche_Route300, df_genou_droit_Route300, df_genou_gauche_Route300, df_hanche_droite_Route300, df_hanche_gauche_Route300
from calcul_vitesses import df_cheville_droite_Route350, df_cheville_gauche_Route350, df_epaule_droite_Route350, df_epaule_gauche_Route350, df_genou_droit_Route350, df_genou_gauche_Route350, df_hanche_droite_Route350, df_hanche_gauche_Route350


########################################################################################

# FONCTIONS UTILES

def vitesse_max_en_valeur_absolue(dataframe, colonne):
    return np.max(np.abs(dataframe[colonne]))

########################################################################################

# On va commencer par caluler pour chaque puissance les valeurs pour la cheville droite

dataframe_a_parcourir_cheville_droite = {
    "Chrono250": df_cheville_droite_Chrono250,
    "Chrono300": df_cheville_droite_Chrono300,
    "Chrono350": df_cheville_droite_Chrono350,
    "Route250": df_cheville_droite_Route250,
    "Route300": df_cheville_droite_Route300,
    "Route350": df_cheville_droite_Route350
}

max_cheville_droite = {}

for nom, dataframe in dataframe_a_parcourir_cheville_droite.items():
    max_cheville_droite[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

# On fait maintenant pour la cheville gauche

dataframe_a_parcourir_cheville_gauche = {
    "Chrono250": df_cheville_gauche_Chrono250,
    "Chrono300": df_cheville_gauche_Chrono300,
    "Chrono350": df_cheville_gauche_Chrono350,
    "Route250": df_cheville_gauche_Route250,
    "Route300": df_cheville_gauche_Route300,
    "Route350": df_cheville_gauche_Route350
}

max_cheville_gauche = {}

for nom, dataframe in dataframe_a_parcourir_cheville_gauche.items():
    max_cheville_gauche[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

# On fait maintenant pour le genou droit

dataframe_a_parcourir_genou_droit = {
    "Chrono250": df_genou_droit_Chrono250,
    "Chrono300": df_genou_droit_Chrono300,
    "Chrono350": df_genou_droit_Chrono350,
    "Route250": df_genou_droit_Route250,
    "Route300": df_genou_droit_Route300,
    "Route350": df_genou_droit_Route350
}

max_genou_droit = {}

for nom, dataframe in dataframe_a_parcourir_genou_droit.items():
    max_genou_droit[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

# Puis le genou gauche

dataframe_a_parcourir_genou_gauche = {
    "Chrono250": df_genou_gauche_Chrono250,
    "Chrono300": df_genou_gauche_Chrono300,
    "Chrono350": df_genou_gauche_Chrono350,
    "Route250": df_genou_gauche_Route250,
    "Route300": df_genou_gauche_Route300,
    "Route350": df_genou_gauche_Route350
}

max_genou_gauche = {}

for nom, dataframe in dataframe_a_parcourir_genou_gauche.items():
    max_genou_gauche[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

# Puis la hanche droite

dataframe_a_parcourir_hanche_droite = {
    "Chrono250": df_hanche_droite_Chrono250,
    "Chrono300": df_hanche_droite_Chrono300,
    "Chrono350": df_hanche_droite_Chrono350,
    "Route250": df_hanche_droite_Route250,
    "Route300": df_hanche_droite_Route300,
    "Route350": df_hanche_droite_Route350
}

max_hanche_droite = {}

for nom, dataframe in dataframe_a_parcourir_hanche_droite.items():
    max_hanche_droite[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

# Puis la hanche gauche

dataframe_a_parcourir_hanche_gauche = {
    "Chrono250": df_hanche_gauche_Chrono250,
    "Chrono300": df_hanche_gauche_Chrono300,
    "Chrono350": df_hanche_gauche_Chrono350,
    "Route250": df_hanche_gauche_Route250,
    "Route300": df_hanche_gauche_Route300,
    "Route350": df_hanche_gauche_Route350
}

max_hanche_gauche = {}

for nom, dataframe in dataframe_a_parcourir_hanche_gauche.items():
    max_hanche_gauche[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

########################################################################################

# Etudions l'épaule plus en détail

# Onn calcule le max pour l'épaule droite

dataframe_a_parcourir_epaule_droite = {
    "Chrono250": df_epaule_droite_Chrono250,
    "Chrono300": df_epaule_droite_Chrono300,
    "Chrono350": df_epaule_droite_Chrono350,
    "Route250": df_epaule_droite_Route250,
    "Route300": df_epaule_droite_Route300,
    "Route350": df_epaule_droite_Route350
}

max_epaule_droite = {}

for nom, dataframe in dataframe_a_parcourir_epaule_droite.items():
    max_epaule_droite[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

# Puis pour l'épaule gauche

dataframe_a_parcourir_epaule_gauche = {
    "Chrono250": df_epaule_gauche_Chrono250,
    "Chrono300": df_epaule_gauche_Chrono300,
    "Chrono350": df_epaule_gauche_Chrono350,
    "Route250": df_epaule_gauche_Route250,
    "Route300": df_epaule_gauche_Route300,
    "Route350": df_epaule_gauche_Route350
}

max_epaule_gauche = {}

for nom, dataframe in dataframe_a_parcourir_epaule_gauche.items():
    max_epaule_gauche[nom] = vitesse_max_en_valeur_absolue(dataframe, "Vitesse angulaire")

# On calcule aussi la moyenne pour l'épaule droite

moy_droite_Chrono250 = np.mean(np.abs(df_epaule_droite_Chrono250["Vitesse angulaire"]))
moy_droite_Chrono300 = np.mean(np.abs(df_epaule_droite_Chrono300["Vitesse angulaire"]))
moy_droite_Chrono350 = np.mean(np.abs(df_epaule_droite_Chrono350["Vitesse angulaire"]))
moy_droite_Route250 = np.mean(np.abs(df_epaule_droite_Route250["Vitesse angulaire"]))
moy_droite_Route300 = np.mean(np.abs(df_epaule_droite_Route300["Vitesse angulaire"]))
moy_droite_Route350 = np.mean(np.abs(df_epaule_droite_Route350["Vitesse angulaire"]))

# On calcule aussi la moyenne pour l'épaule gauche

moy_gauche_Chrono250 = np.mean(np.abs(df_epaule_gauche_Chrono250["Vitesse angulaire"]))
moy_gauche_Chrono300 = np.mean(np.abs(df_epaule_gauche_Chrono300["Vitesse angulaire"]))
moy_gauche_Chrono350 = np.mean(np.abs(df_epaule_gauche_Chrono350["Vitesse angulaire"]))
moy_gauche_Route250 = np.mean(np.abs(df_epaule_gauche_Route250["Vitesse angulaire"]))
moy_gauche_Route300 = np.mean(np.abs(df_epaule_gauche_Route300["Vitesse angulaire"]))
moy_gauche_Route350 = np.mean(np.abs(df_epaule_gauche_Route350["Vitesse angulaire"]))

# On calcule aussi l'écart-type pour l'épaule droite

std_droite_Chrono250 = np.std(df_epaule_droite_Chrono250["Vitesse angulaire"])
std_droite_Chrono300 = np.std(df_epaule_droite_Chrono300["Vitesse angulaire"])
std_droite_Chrono350 = np.std(df_epaule_droite_Chrono350["Vitesse angulaire"])
std_droite_Route250 = np.std(df_epaule_droite_Route250["Vitesse angulaire"])
std_droite_Route300 = np.std(df_epaule_droite_Route300["Vitesse angulaire"])
std_droite_Route350 = np.std(df_epaule_droite_Route350["Vitesse angulaire"])

# On calcule aussi l'écart-type pour l'épaule gauche

std_gauche_Chrono250 = np.std(df_epaule_gauche_Chrono250["Vitesse angulaire"])
std_gauche_Chrono300 = np.std(df_epaule_gauche_Chrono300["Vitesse angulaire"])
std_gauche_Chrono350 = np.std(df_epaule_gauche_Chrono350["Vitesse angulaire"])
std_gauche_Route250 = np.std(df_epaule_gauche_Route250["Vitesse angulaire"])
std_gauche_Route300 = np.std(df_epaule_gauche_Route300["Vitesse angulaire"])
std_gauche_Route350 = np.std(df_epaule_gauche_Route350["Vitesse angulaire"])
