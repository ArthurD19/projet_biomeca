from calcul_angles import df_angles_Chrono250
from calcul_angles import df_angles_Chrono300
from calcul_angles import df_angles_Chrono350
from calcul_angles import df_angles_Route250
from calcul_angles import df_angles_Route300
from calcul_angles import df_angles_Route350

frequence = 60  # Hz la fréquence d'échantillonnage

# On commence par calculer les vitesses pour Chrono250

df_hanche_droite_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Hanche droite"].sort_values(by=["Frame"])
df_hanche_droite_Chrono250["Vitesse angulaire"] = df_hanche_droite_Chrono250["Angle"].diff() / (1 / 60)

df_hanche_gauche_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Hanche gauche"].sort_values(by=["Frame"])
df_hanche_gauche_Chrono250["Vitesse angulaire"] = df_hanche_gauche_Chrono250["Angle"].diff() / (1 / 60)

df_genou_droit_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Genou droit"].sort_values(by=["Frame"])
df_genou_droit_Chrono250["Vitesse angulaire"] = df_genou_droit_Chrono250["Angle"].diff() / (1 / 60)

df_genou_gauche_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Genou gauche"].sort_values(by=["Frame"])
df_genou_gauche_Chrono250["Vitesse angulaire"] = df_genou_gauche_Chrono250["Angle"].diff() / (1 / 60)

df_epaule_droite_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Epaule droite"].sort_values(by=["Frame"])
df_epaule_droite_Chrono250["Vitesse angulaire"] = df_epaule_droite_Chrono250["Angle"].diff() / (1 / 60)

df_epaule_gauche_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Epaule gauche"].sort_values(by=["Frame"])
df_epaule_gauche_Chrono250["Vitesse angulaire"] = df_epaule_gauche_Chrono250["Angle"].diff() / (1 / 60)

df_cheville_droite_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Cheville droite"].sort_values(by=["Frame"])
df_cheville_droite_Chrono250["Vitesse angulaire"] = df_cheville_droite_Chrono250["Angle"].diff() / (1 / 60)

df_cheville_gauche_Chrono250 = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == "Cheville gauche"].sort_values(by=["Frame"])
df_cheville_gauche_Chrono250["Vitesse angulaire"] = df_cheville_gauche_Chrono250["Angle"].diff() / (1 / 60)

# On le fait maintenant pour Chrono300

df_hanche_droite_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Hanche droite"].sort_values(by=["Frame"])
df_hanche_droite_Chrono300["Vitesse angulaire"] = df_hanche_droite_Chrono300["Angle"].diff() / (1 / 60)

df_hanche_gauche_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Hanche gauche"].sort_values(by=["Frame"])
df_hanche_gauche_Chrono300["Vitesse angulaire"] = df_hanche_gauche_Chrono300["Angle"].diff() / (1 / 60)

df_genou_droit_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Genou droit"].sort_values(by=["Frame"])
df_genou_droit_Chrono300["Vitesse angulaire"] = df_genou_droit_Chrono300["Angle"].diff() / (1 / 60)

df_genou_gauche_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Genou gauche"].sort_values(by=["Frame"])
df_genou_gauche_Chrono300["Vitesse angulaire"] = df_genou_gauche_Chrono300["Angle"].diff() / (1 / 60)

df_epaule_droite_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Epaule droite"].sort_values(by=["Frame"])
df_epaule_droite_Chrono300["Vitesse angulaire"] = df_epaule_droite_Chrono300["Angle"].diff() / (1 / 60)

df_epaule_gauche_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Epaule gauche"].sort_values(by=["Frame"])
df_epaule_gauche_Chrono300["Vitesse angulaire"] = df_epaule_gauche_Chrono300["Angle"].diff() / (1 / 60)

df_cheville_droite_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Cheville droite"].sort_values(by=["Frame"])
df_cheville_droite_Chrono300["Vitesse angulaire"] = df_cheville_droite_Chrono300["Angle"].diff() / (1 / 60)

df_cheville_gauche_Chrono300 = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == "Cheville gauche"].sort_values(by=["Frame"])
df_cheville_gauche_Chrono300["Vitesse angulaire"] = df_cheville_gauche_Chrono300["Angle"].diff() / (1 / 60)

# Puis avec Chrono350

df_hanche_droite_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Hanche droite"].sort_values(by=["Frame"])
df_hanche_droite_Chrono350["Vitesse angulaire"] = df_hanche_droite_Chrono350["Angle"].diff() / (1 / 60)

df_hanche_gauche_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Hanche gauche"].sort_values(by=["Frame"])
df_hanche_gauche_Chrono350["Vitesse angulaire"] = df_hanche_gauche_Chrono350["Angle"].diff() / (1 / 60)

df_genou_droit_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Genou droit"].sort_values(by=["Frame"])
df_genou_droit_Chrono350["Vitesse angulaire"] = df_genou_droit_Chrono350["Angle"].diff() / (1 / 60)

df_genou_gauche_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Genou gauche"].sort_values(by=["Frame"])
df_genou_gauche_Chrono350["Vitesse angulaire"] = df_genou_gauche_Chrono350["Angle"].diff() / (1 / 60)

df_epaule_droite_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Epaule droite"].sort_values(by=["Frame"])
df_epaule_droite_Chrono350["Vitesse angulaire"] = df_epaule_droite_Chrono350["Angle"].diff() / (1 / 60)

df_epaule_gauche_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Epaule gauche"].sort_values(by=["Frame"])
df_epaule_gauche_Chrono350["Vitesse angulaire"] = df_epaule_gauche_Chrono350["Angle"].diff() / (1 / 60)

df_cheville_droite_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Cheville droite"].sort_values(by=["Frame"])
df_cheville_droite_Chrono350["Vitesse angulaire"] = df_cheville_droite_Chrono350["Angle"].diff() / (1 / 60)

df_cheville_gauche_Chrono350 = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == "Cheville gauche"].sort_values(by=["Frame"])
df_cheville_gauche_Chrono350["Vitesse angulaire"] = df_cheville_gauche_Chrono350["Angle"].diff() / (1 / 60)

# On passe à Route250

df_hanche_droite_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Hanche droite"].sort_values(by=["Frame"])
df_hanche_droite_Route250["Vitesse angulaire"] = df_hanche_droite_Route250["Angle"].diff() / (1 / 60)

df_hanche_gauche_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Hanche gauche"].sort_values(by=["Frame"])
df_hanche_gauche_Route250["Vitesse angulaire"] = df_hanche_gauche_Route250["Angle"].diff() / (1 / 60)

df_genou_droit_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Genou droit"].sort_values(by=["Frame"])
df_genou_droit_Route250["Vitesse angulaire"] = df_genou_droit_Route250["Angle"].diff() / (1 / 60)

df_genou_gauche_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Genou gauche"].sort_values(by=["Frame"])
df_genou_gauche_Route250["Vitesse angulaire"] = df_genou_gauche_Route250["Angle"].diff() / (1 / 60)

df_epaule_droite_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Epaule droite"].sort_values(by=["Frame"])
df_epaule_droite_Route250["Vitesse angulaire"] = df_epaule_droite_Route250["Angle"].diff() / (1 / 60)

df_epaule_gauche_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Epaule gauche"].sort_values(by=["Frame"])
df_epaule_gauche_Route250["Vitesse angulaire"] = df_epaule_gauche_Route250["Angle"].diff() / (1 / 60)

df_cheville_droite_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Cheville droite"].sort_values(by=["Frame"])
df_cheville_droite_Route250["Vitesse angulaire"] = df_cheville_droite_Route250["Angle"].diff() / (1 / 60)

df_cheville_gauche_Route250 = df_angles_Route250[df_angles_Route250["Articulation"] == "Cheville gauche"].sort_values(by=["Frame"])
df_cheville_gauche_Route250["Vitesse angulaire"] = df_cheville_gauche_Route250["Angle"].diff() / (1 / 60)

# Maintenant, on s'occupe de Route300

df_hanche_droite_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Hanche droite"].sort_values(by=["Frame"])
df_hanche_droite_Route300["Vitesse angulaire"] = df_hanche_droite_Route300["Angle"].diff() / (1 / 60)

df_hanche_gauche_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Hanche gauche"].sort_values(by=["Frame"])
df_hanche_gauche_Route300["Vitesse angulaire"] = df_hanche_gauche_Route300["Angle"].diff() / (1 / 60)

df_genou_droit_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Genou droit"].sort_values(by=["Frame"])
df_genou_droit_Route300["Vitesse angulaire"] = df_genou_droit_Route300["Angle"].diff() / (1 / 60)

df_genou_gauche_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Genou gauche"].sort_values(by=["Frame"])
df_genou_gauche_Route300["Vitesse angulaire"] = df_genou_gauche_Route300["Angle"].diff() / (1 / 60)

df_epaule_droite_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Epaule droite"].sort_values(by=["Frame"])
df_epaule_droite_Route300["Vitesse angulaire"] = df_epaule_droite_Route300["Angle"].diff() / (1 / 60)

df_epaule_gauche_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Epaule gauche"].sort_values(by=["Frame"])
df_epaule_gauche_Route300["Vitesse angulaire"] = df_epaule_gauche_Route300["Angle"].diff() / (1 / 60)

df_cheville_droite_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Cheville droite"].sort_values(by=["Frame"])
df_cheville_droite_Route300["Vitesse angulaire"] = df_cheville_droite_Route300["Angle"].diff() / (1 / 60)

df_cheville_gauche_Route300 = df_angles_Route300[df_angles_Route300["Articulation"] == "Cheville gauche"].sort_values(by=["Frame"])
df_cheville_gauche_Route300["Vitesse angulaire"] = df_cheville_gauche_Route300["Angle"].diff() / (1 / 60)

# Maintenant, on termine par Route350

df_hanche_droite_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Hanche droite"].sort_values(by=["Frame"])
df_hanche_droite_Route350["Vitesse angulaire"] = df_hanche_droite_Route350["Angle"].diff() / (1 / 60)

df_hanche_gauche_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Hanche gauche"].sort_values(by=["Frame"])
df_hanche_gauche_Route350["Vitesse angulaire"] = df_hanche_gauche_Route350["Angle"].diff() / (1 / 60)

df_genou_droit_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Genou droit"].sort_values(by=["Frame"])
df_genou_droit_Route350["Vitesse angulaire"] = df_genou_droit_Route350["Angle"].diff() / (1 / 60)

df_genou_gauche_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Genou gauche"].sort_values(by=["Frame"])
df_genou_gauche_Route350["Vitesse angulaire"] = df_genou_gauche_Route350["Angle"].diff() / (1 / 60)

df_epaule_droite_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Epaule droite"].sort_values(by=["Frame"])
df_epaule_droite_Route350["Vitesse angulaire"] = df_epaule_droite_Route350["Angle"].diff() / (1 / 60)

df_epaule_gauche_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Epaule gauche"].sort_values(by=["Frame"])
df_epaule_gauche_Route350["Vitesse angulaire"] = df_epaule_gauche_Route350["Angle"].diff() / (1 / 60)

df_cheville_droite_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Cheville droite"].sort_values(by=["Frame"])
df_cheville_droite_Route350["Vitesse angulaire"] = df_cheville_droite_Route350["Angle"].diff() / (1 / 60)

df_cheville_gauche_Route350 = df_angles_Route350[df_angles_Route350["Articulation"] == "Cheville gauche"].sort_values(by=["Frame"])
df_cheville_gauche_Route350["Vitesse angulaire"] = df_cheville_gauche_Route350["Angle"].diff() / (1 / 60)
