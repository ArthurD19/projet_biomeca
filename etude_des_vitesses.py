import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

#################################################################################

# Mettons maintenant en forme tout cela (effet de la puissance)

puissances = [250, 300, 350]

# On commence par le genou droite

genou_droit_chrono = [
    max_genou_droit["Chrono250"],
    max_genou_droit["Chrono300"],
    max_genou_droit["Chrono350"]
]

genou_droit_route = [
    max_genou_droit["Route250"],
    max_genou_droit["Route300"],
    max_genou_droit["Route350"]
]

plt.figure()
plt.plot(puissances, genou_droit_chrono, marker='o', label="Chrono")
plt.plot(puissances, genou_droit_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Genou droit – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance genou droit.png")
plt.show()

# puis le genou gauche

genou_gauche_chrono = [
    max_genou_gauche["Chrono250"],
    max_genou_gauche["Chrono300"],
    max_genou_gauche["Chrono350"]
]

genou_gauche_route = [
    max_genou_gauche["Route250"],
    max_genou_gauche["Route300"],
    max_genou_gauche["Route350"]
]

plt.figure()
plt.plot(puissances, genou_gauche_chrono, marker='o', label="Chrono")
plt.plot(puissances, genou_gauche_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Genou gauche – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance genou gauche.png")
plt.show()

# Puis la hanche droite

hanche_droite_chrono = [
    max_hanche_droite["Chrono250"],
    max_hanche_droite["Chrono300"],
    max_hanche_droite["Chrono350"]
]

hanche_droite_route = [
    max_hanche_droite["Route250"],
    max_hanche_droite["Route300"],
    max_hanche_droite["Route350"]
]

plt.figure()
plt.plot(puissances, hanche_droite_chrono, marker='o', label="Chrono")
plt.plot(puissances, hanche_droite_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Hanche droite – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance hanche droite.png")
plt.show()

# puis la hanche gauche

hanche_gauche_chrono = [
    max_hanche_gauche["Chrono250"],
    max_hanche_gauche["Chrono300"],
    max_hanche_gauche["Chrono350"]
]

hanche_gauche_route = [
    max_hanche_gauche["Route250"],
    max_hanche_gauche["Route300"],
    max_hanche_gauche["Route350"]
]

plt.figure()
plt.plot(puissances, hanche_gauche_chrono, marker='o', label="Chrono")
plt.plot(puissances, hanche_gauche_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Hanche gauche – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance hanche gauche.png")
plt.show()

# Puis la cheville droite

cheville_droite_chrono = [
    max_cheville_droite["Chrono250"],
    max_cheville_droite["Chrono300"],
    max_cheville_droite["Chrono350"]
]

cheville_droite_route = [
    max_cheville_droite["Route250"],
    max_cheville_droite["Route300"],
    max_cheville_droite["Route350"]
]

plt.figure()
plt.plot(puissances, cheville_droite_chrono, marker='o', label="Chrono")
plt.plot(puissances, cheville_droite_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Cheville droite – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance cheville droite.png")
plt.show()

# puis la cheville gauche

cheville_gauche_chrono = [
    max_cheville_gauche["Chrono250"],
    max_cheville_gauche["Chrono300"],
    max_cheville_gauche["Chrono350"]
]

cheville_gauche_route = [
    max_cheville_gauche["Route250"],
    max_cheville_gauche["Route300"],
    max_cheville_gauche["Route350"]
]

plt.figure()
plt.plot(puissances, cheville_gauche_chrono, marker='o', label="Chrono")
plt.plot(puissances, cheville_gauche_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Cheville gauche – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance cheville gauche.png")
plt.show()


###################################################################################

# Maintenant, illustrons les résultats spécifiques aux épaules

# On commence par le max pour l'épaule droite

epaule_droite_chrono = [
    max_epaule_droite["Chrono250"],
    max_epaule_droite["Chrono300"],
    max_epaule_droite["Chrono350"]
]

epaule_droite_route = [
    max_epaule_droite["Route250"],
    max_epaule_droite["Route300"],
    max_epaule_droite["Route350"]
]

plt.figure()
plt.plot(puissances, epaule_droite_chrono, marker='o', label="Chrono")
plt.plot(puissances, epaule_droite_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Epaule droite – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance epaule droite.png")
plt.show()

# puis le max pour l'épaule gauche

epaule_gauche_chrono = [
    max_epaule_gauche["Chrono250"],
    max_epaule_gauche["Chrono300"],
    max_epaule_gauche["Chrono350"]
]

epaule_gauche_route = [
    max_epaule_gauche["Route250"],
    max_epaule_gauche["Route300"],
    max_epaule_gauche["Route350"]
]

plt.figure()
plt.plot(puissances, epaule_gauche_chrono, marker='o', label="Chrono")
plt.plot(puissances, epaule_gauche_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse angulaire max |ω|")
plt.title("Epaule gauche – effet de la puissance")
plt.legend()
plt.grid(True)
plt.savefig("résultats/effet puissance epaule gauche.png")
plt.show()

# On passe ensuite à la moyenne pour l'épaule droite

moy_epaule_droite_chrono = [
    moy_droite_Chrono250,
    moy_droite_Chrono300,
    moy_droite_Chrono350
]

moy_epaule_droite_route = [
    moy_droite_Route250,
    moy_droite_Route300,
    moy_droite_Route350
]

plt.figure()
plt.plot(puissances, moy_epaule_droite_chrono, marker='o', label="Chrono")
plt.plot(puissances, moy_epaule_droite_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse moyenne |ω|")
plt.title("Épaule droite – activité posturale moyenne")
plt.legend()
plt.grid(True)
plt.savefig("résultats/vitesse moy epaule droite.png")
plt.show()

# On passe ensuite à la moyenne pour l'épaule gauche

moy_epaule_gauche_chrono = [
    moy_gauche_Chrono250,
    moy_gauche_Chrono300,
    moy_gauche_Chrono350
]

moy_epaule_gauche_route = [
    moy_gauche_Route250,
    moy_gauche_Route300,
    moy_gauche_Route350
]

plt.figure()
plt.plot(puissances, moy_epaule_gauche_chrono, marker='o', label="Chrono")
plt.plot(puissances, moy_epaule_gauche_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Vitesse moyenne |ω|")
plt.title("Épaule gauche – activité posturale moyenne")
plt.legend()
plt.grid(True)
plt.savefig("résultats/vitesse moy epaule gauche.png")
plt.show()

# On finit par l'écart-type épaule droite

std_epaule_droite_chrono = [
    std_droite_Chrono250,
    std_droite_Chrono300,
    std_droite_Chrono350
]

std_epaule_droite_route = [
    std_droite_Route250,
    std_droite_Route300,
    std_droite_Route350
]

plt.figure()
plt.plot(puissances, std_epaule_droite_chrono, marker='o', label="Chrono")
plt.plot(puissances, std_epaule_droite_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Écart-type de ω")
plt.title("Épaule droite – variabilité de la vitesse")
plt.legend()
plt.grid(True)
plt.savefig("résultats/ecart type vitesse epaule droite.png")
plt.show()

# Et épaule gauche

std_epaule_gauche_chrono = [
    std_gauche_Chrono250,
    std_gauche_Chrono300,
    std_gauche_Chrono350
]

std_epaule_gauche_route = [
    std_gauche_Route250,
    std_gauche_Route300,
    std_gauche_Route350
]

plt.figure()
plt.plot(puissances, std_epaule_gauche_chrono, marker='o', label="Chrono")
plt.plot(puissances, std_epaule_gauche_route, marker='o', label="Route")
plt.xlabel("Puissance (W)")
plt.ylabel("Écart-type de ω")
plt.title("Épaule gauche – variabilité de la vitesse")
plt.legend()
plt.grid(True)
plt.savefig("résultats/ecart type vitesse epaule gauche.png")
plt.show()
