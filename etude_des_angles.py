import pandas as pd

from calcul_angles import df_angles_Chrono250
from calcul_angles import df_angles_Chrono300
from calcul_angles import df_angles_Chrono350
from calcul_angles import df_angles_Route250
from calcul_angles import df_angles_Route300
from calcul_angles import df_angles_Route350


# On commence par étudier les maximum, le minimum et la différence maximum - minimum
# pour Chrono250
results_Chrono250 = []
print("Chrono250")
for articulation in df_angles_Chrono250["Articulation"].unique():
    angles = df_angles_Chrono250[df_angles_Chrono250["Articulation"] == articulation]["Angle"]
    maximum = angles.max()
    minimum = angles.min()
    difference = maximum - minimum
    results_Chrono250.append({
        "Articulation": articulation,
        "Maximum": maximum,
        "Minimum": minimum,
        "RoM": difference
    })
df_results_Chrono250 = pd.DataFrame(results_Chrono250)
print(df_results_Chrono250.to_string(index=False))

# On le fait maintenant pour Chrono300
results_Chrono300 = []
print("Chrono300")
for articulation in df_angles_Chrono300["Articulation"].unique():
    angles = df_angles_Chrono300[df_angles_Chrono300["Articulation"] == articulation]["Angle"]
    maximum = angles.max()
    minimum = angles.min()
    difference = maximum - minimum
    results_Chrono300.append({
        "Articulation": articulation,
        "Maximum": maximum,
        "Minimum": minimum,
        "RoM": difference
    })
df_results_Chrono300 = pd.DataFrame(results_Chrono300)
print(df_results_Chrono300.to_string(index=False))

# Puis pour Chrono350
results_Chrono350 = []
print("Chrono350")
for articulation in df_angles_Chrono350["Articulation"].unique():
    angles = df_angles_Chrono350[df_angles_Chrono350["Articulation"] == articulation]["Angle"]
    maximum = angles.max()
    minimum = angles.min()
    difference = maximum - minimum
    results_Chrono350.append({
        "Articulation": articulation,
        "Maximum": maximum,
        "Minimum": minimum,
        "RoM": difference
    })
df_results_Chrono350 = pd.DataFrame(results_Chrono350)
print(df_results_Chrono350.to_string(index=False))

# On passe à Route250
results_Route250 = []
print("Route250")
for articulation in df_angles_Route250["Articulation"].unique():
    angles = df_angles_Route250[df_angles_Route250["Articulation"] == articulation]["Angle"]
    maximum = angles.max()
    minimum = angles.min()
    difference = maximum - minimum
    results_Route250.append({
        "Articulation": articulation,
        "Maximum": maximum,
        "Minimum": minimum,
        "RoM": difference
    })
df_results_Route250 = pd.DataFrame(results_Route250)
print(df_results_Route250.to_string(index=False))

# Puis on fait Route300
results_Route300 = []
print("Route300")
for articulation in df_angles_Route300["Articulation"].unique():
    angles = df_angles_Route300[df_angles_Route300["Articulation"] == articulation]["Angle"]
    maximum = angles.max()
    minimum = angles.min()
    difference = maximum - minimum
    results_Route300.append({
        "Articulation": articulation,
        "Maximum": maximum,
        "Minimum": minimum,
        "RoM": difference
    })
df_results_Route300 = pd.DataFrame(results_Route300)
print(df_results_Route300.to_string(index=False))

# On termine par Route350
results_Route350 = []
print("Route350")
for articulation in df_angles_Route350["Articulation"].unique():
    angles = df_angles_Route350[df_angles_Route350["Articulation"] == articulation]["Angle"]
    maximum = angles.max()
    minimum = angles.min()
    difference = maximum - minimum
    results_Route350.append({
        "Articulation": articulation,
        "Maximum": maximum,
        "Minimum": minimum,
        "RoM": difference
    })
df_results_Route350 = pd.DataFrame(results_Route350)
print(df_results_Route350.to_string(index=False))

import matplotlib.pyplot as plt

# Regroupement des données pour le graphisme (exemple pour le RoM)
# Vous pouvez créer un DataFrame global regroupant vos df_results_...
all_results = pd.concat([
    df_results_Chrono250.assign(Pos='Chrono', P=250),
    df_results_Chrono300.assign(Pos='Chrono', P=300),
    df_results_Chrono350.assign(Pos='Chrono', P=350),
    df_results_Route250.assign(Pos='Route', P=250),
    df_results_Route300.assign(Pos='Route', P=300),
    df_results_Route350.assign(Pos='Route', P=350)
])

# Graphique 1 : Comparaison du RoM Moyen
rom_avg = all_results.groupby(['Pos', 'Articulation'])['RoM'].mean().unstack(level=0)
rom_avg.plot(kind='bar', figsize=(10, 6))
plt.title('Comparaison du RoM Moyen : Route vs Chrono')
plt.ylabel('Degrés')
plt.savefig('rom_comparison.png')

# Graphique 2 : Evolution de la Hanche Minimum
hanche_min = all_results[all_results['Articulation'].str.contains('Hanche')].pivot_table(index='P', columns=['Pos', 'Articulation'], values='Minimum')
hanche_min.plot(marker='o', figsize=(10, 6))
plt.title('Angle de Hanche Minimum vs Puissance')
plt.ylabel('Degrés')
plt.savefig('hanche_min_power.png')
