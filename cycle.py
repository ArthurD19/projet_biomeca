import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- IMPORTATION ---
from calcul_angles import (df_angles_Chrono250, df_angles_Chrono300, df_angles_Chrono350,
                           df_angles_Route250, df_angles_Route300, df_angles_Route350)

datasets = {
    'Chrono 250W': df_angles_Chrono250, 'Chrono 300W': df_angles_Chrono300, 'Chrono 350W': df_angles_Chrono350,
    'Route 250W': df_angles_Route250, 'Route 300W': df_angles_Route300, 'Route 350W': df_angles_Route350
}

def plot_cycle_comparaison_synchro(nom_recherche):
    plt.figure(figsize=(10, 6))
    styles = {
        'Chrono 250W': ('#1f77b4', '-'), 'Chrono 300W': ('#41a1e1', '-'), 'Chrono 350W': ('#004c8c', '-'),
        'Route 250W': ('#ff7f0e', '--'), 'Route 300W': ('#ffbb78', '--'), 'Route 350W': ('#bd3e00', '--')
    }

    found_any = False
    for label, df in datasets.items():
        df = pd.DataFrame(df)
        mask = df['Articulation'].str.contains(nom_recherche, case=False, na=False)
        data_art = df[mask]['Angle'].values

        if len(data_art) > 150:
            found_any = True
            # On prend une fenêtre assez large pour trouver un cycle complet
            segment = data_art[100:250]

            # --- SYNCHRONISATION ---
            # On trouve l'indice du pic (le maximum d'angle)
            idx_max = np.argmax(segment)
            # On recrée un cycle de 100 points en commençant à ce pic
            # Cela permet de superposer tous les "hauts" de courbes
            cycle_synchro = data_art[100 + idx_max : 100 + idx_max + 100]

            x_norm = np.linspace(0, 100, len(cycle_synchro))
            color, linestyle = styles[label]
            plt.plot(x_norm, cycle_synchro, label=label, color=color, linestyle=linestyle, linewidth=2)

    if not found_any:
        print(f"ERREUR : Aucun nom contenant '{nom_recherche}' trouvé.")
        return

    plt.title(f'Comparaison Synchronisée : {nom_recherche}')
    plt.xlabel('Cycle de pédalage normalisé (0-100%)')
    plt.ylabel('Angle (degrés)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f"cycle_synchro_{nom_recherche}.png")
    plt.show()

# --- GÉNÉRATION ---
plot_cycle_comparaison_synchro('Genou D')
plot_cycle_comparaison_synchro('Hanche D')
plot_cycle_comparaison_synchro('Epaule D')
plot_cycle_comparaison_synchro('Cheville D')
