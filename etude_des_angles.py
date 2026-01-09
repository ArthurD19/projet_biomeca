import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

<<<<<<< HEAD
# AUTRE TEST DE GRAPHE

# On crée le DataFrame global à partir de vos données
all_data = pd.concat([
    df_results_Chrono250.assign(Position='Chrono', Puissance='250W'),
    df_results_Chrono300.assign(Position='Chrono', Puissance='300W'),
    df_results_Chrono350.assign(Position='Chrono', Puissance='350W'),
    df_results_Route250.assign(Position='Route', Puissance='250W'),
    df_results_Route300.assign(Position='Route', Puissance='300W'),
    df_results_Route350.assign(Position='Route', Puissance='350W')
])

# Filtrer pour ne garder que les articulations principales (membres inférieurs + épaule)
mask = all_data['Articulation'].isin(['Hanche droite', 'Genou droit', 'Cheville droite','Epaule droite','Hanche gauche', 'Genou gauche', 'Cheville gauche', 'Epaule gauche'])
df_plot = all_data[mask]

# Création du graphique comparatif détaillé
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), sharey=True)

# Graphique pour la Route
df_plot[df_plot['Position'] == 'Route'].pivot(index='Articulation', columns='Puissance', values='RoM').plot(kind='bar', ax=ax1)
ax1.set_title('RoM par Puissance - Position ROUTE')
ax1.set_ylabel('Amplitude (degrés)')

# Graphique pour le Chrono
df_plot[df_plot['Position'] == 'Chrono'].pivot(index='Articulation', columns='Puissance', values='RoM').plot(kind='bar', ax=ax2)
ax2.set_title('RoM par Puissance - Position CHRONO')

plt.tight_layout()
plt.savefig('rom_detail_puissance.png')
plt.show()
=======
# Graphiques suite


def plot_joint_detailed(df, joint_name, save_prefix=''):
    """
    Crée 3 graphiques (min, max, ROM) pour une articulation donnée
    avec barres groupées par type de vélo pour chaque puissance
    """
    # Filtrer les données pour cette articulation
    df_joint = df[df['Articulation'] == joint_name].copy()
    
    if df_joint.empty:
        print(f"Attention : aucune donnée pour {joint_name}")
        return
    
    # Créer la figure avec 3 sous-graphiques
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle(f'{joint_name} - Comparaison Route vs CLM', 
                 fontsize=16, fontweight='bold', y=1.02)
    
    metrics = ['Minimum', 'Maximum', 'RoM']
    colors = {'Chrono': '#FF6B6B', 'Route': '#4ECDC4'}
    
    for idx, metric in enumerate(metrics):
        ax = axes[idx]
        
        # Préparer les données pour le graphique
        puissances = sorted(df_joint['P'].unique())
        x = np.arange(len(puissances))
        width = 0.35
        
        # Données CLM et Route
        clm_data = df_joint[df_joint['Pos'] == 'Chrono'].sort_values('P')[metric].values
        route_data = df_joint[df_joint['Pos'] == 'Route'].sort_values('P')[metric].values
        
        # Créer les barres
        bars1 = ax.bar(x - width/2, clm_data, width, label='Chrono', 
                       color=colors['Chrono'], alpha=0.8, edgecolor='black', linewidth=1.2)
        bars2 = ax.bar(x + width/2, route_data, width, label='Route', 
                       color=colors['Route'], alpha=0.8, edgecolor='black', linewidth=1.2)
        
        # Ajouter les valeurs sur les barres
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.1f}°',
                       ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        # Mise en forme
        ax.set_xlabel('Intensité', fontsize=12, fontweight='bold')
        ax.set_ylabel(f'{metric} (°)', fontsize=12, fontweight='bold')
        ax.set_title(metric, fontsize=13, fontweight='bold')
        ax.set_xticks(x)
        ax.set_xticklabels([f'{int(p)}W' for p in puissances], fontsize=11)
        ax.legend(loc='best', fontsize=11, framealpha=0.9)
        ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=0.8)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        
        # Ajuster les limites y pour laisser de l'espace pour les annotations
        ymin, ymax = ax.get_ylim()
        ax.set_ylim(ymin, ymax * 1.12)
    
    plt.tight_layout()
    
    if save_prefix:
        filename = f"{save_prefix}_{joint_name.replace(' ', '_')}.png"
        plt.savefig(f"résultats/{filename}", dpi=300, bbox_inches='tight')
        print(f"✓ Graphique sauvegardé : {filename}")
    
    plt.show()

# On génère les premiers graphiques


print("\n" + "="*80)
print("GÉNÉRATION DES GRAPHIQUES PAR ARTICULATION")
print("="*80)

# Liste des articulations à analyser
articulations = all_results['Articulation'].unique()

for articulation in articulations:
    print(f"\n→ Génération pour : {articulation}")
    plot_joint_detailed(all_results, articulation, save_prefix='graph')

# GRAPHIQUE RÉCAPITULATIF : ROM de toutes les articulations


def plot_rom_summary(df, save_name='graph_rom_summary.png'):
    """
    Graphique récapitulatif montrant le ROM de toutes les articulations
    pour chaque intensité
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle('ROM - Comparaison générale Route vs CLM', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    puissances = sorted(df['P'].unique())
    articulations = df['Articulation'].unique()
    colors = {'Chrono': '#FF6B6B', 'Route': '#4ECDC4'}
    
    for idx, puissance in enumerate(puissances):
        ax = axes[idx]
        
        df_power = df[df['P'] == puissance]
        
        x_pos = np.arange(len(articulations))
        width = 0.35
        
        clm_roms = []
        route_roms = []
        
        for art in articulations:
            clm_val = df_power[(df_power['Articulation'] == art) & 
                               (df_power['Pos'] == 'Chrono')]['RoM'].values
            route_val = df_power[(df_power['Articulation'] == art) & 
                                 (df_power['Pos'] == 'Route')]['RoM'].values
            
            clm_roms.append(clm_val[0] if len(clm_val) > 0 else 0)
            route_roms.append(route_val[0] if len(route_val) > 0 else 0)
        
        bars1 = ax.bar(x_pos - width/2, clm_roms, width, label='Chrono', 
                       color=colors['Chrono'], alpha=0.8, edgecolor='black')
        bars2 = ax.bar(x_pos + width/2, route_roms, width, label='Route', 
                       color=colors['Route'], alpha=0.8, edgecolor='black')
        
        ax.set_xlabel('Articulations', fontsize=12, fontweight='bold')
        ax.set_ylabel('ROM (°)', fontsize=12, fontweight='bold')
        ax.set_title(f'{int(puissance)}W', fontsize=13, fontweight='bold')
        ax.set_xticks(x_pos)
        ax.set_xticklabels([art.replace(' droite', '').replace(' gauche', '') 
                            for art in articulations], 
                           rotation=45, ha='right', fontsize=9)
        ax.legend(fontsize=10)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig(f"résultats/{save_name}", dpi=300, bbox_inches='tight')
    print(f"\n✓ Graphique récapitulatif sauvegardé : {save_name}")
    plt.show()


print("\n" + "="*80)
print("GRAPHIQUE RÉCAPITULATIF ROM")
print("="*80)
plot_rom_summary(all_results)


# TABLEAU COMPARATIF : Différences Route - CLM


print("\n" + "="*80)
print("TABLEAU DES DIFFÉRENCES (Route - CLM)")
print("="*80)

for puissance in sorted(all_results['P'].unique()):
    print(f"\n--- {int(puissance)}W ---")
    df_p = all_results[all_results['P'] == puissance]
    
    comparisons = []
    for art in df_p['Articulation'].unique():
        clm = df_p[(df_p['Articulation'] == art) & (df_p['Pos'] == 'Chrono')]
        route = df_p[(df_p['Articulation'] == art) & (df_p['Pos'] == 'Route')]
        
        if not clm.empty and not route.empty:
            diff_rom = route['RoM'].values[0] - clm['RoM'].values[0]
            pct_diff = (diff_rom / clm['RoM'].values[0]) * 100
            
            comparisons.append({
                'Articulation': art,
                'ROM CLM': f"{clm['RoM'].values[0]:.2f}°",
                'ROM Route': f"{route['RoM'].values[0]:.2f}°",
                'Différence': f"{diff_rom:+.2f}°",
                'Δ%': f"{pct_diff:+.1f}%"
            })
    
    df_comp = pd.DataFrame(comparisons)
    print(df_comp.to_string(index=False))

print("\n" + "="*80)
print("✓ GÉNÉRATION TERMINÉE")
print("="*80)
>>>>>>> f800601b235063901bbe80c4e8319520fc2f6d7f
