import pandas as pd
import glob
import os

# --- CONFIGURATION DES CHEMINS ---
dossier_source = "../DATA FOR LEAGUES"
dossier_sortie = "../FINAL DATASET"
nom_fichier_final = "European Top 5 Leagues - Historical Match Data (2015-2025).csv"

print(f"Debut de la fusion avec placement de Saison depuis : {dossier_source}")

# Verification et creation du dossier de sortie
if not os.path.exists(dossier_sortie):
    os.makedirs(dossier_sortie)
    print(f"Dossier '{dossier_sortie}' cree.")

#Lister les fichiers CSV
chemin_recherche = os.path.join(dossier_source, "*.csv")
fichiers_csv = glob.glob(chemin_recherche)
liste_dfs = []

print(f"{len(fichiers_csv)} fichiers trouves. Traitement en cours...")

for fichier in fichiers_csv:
    try:
        df_temp = pd.read_csv(fichier, low_memory=False)

        # --- AJOUT DE LA COLONNE SAISON ---
        nom_base = os.path.basename(fichier)
        if '-' in nom_base:
            parts = nom_base.split('-')
            if len(parts) >= 3:
                saison = parts[1] + "-" + parts[2].replace('.csv', '')
                df_temp['Season'] = saison

        # Ajout a la liste
        liste_dfs.append(df_temp)

    except Exception as e:
        print(f"Erreur sur {fichier} : {e}")

#Concatenation
if liste_dfs:
    df_final = pd.concat(liste_dfs, ignore_index=True)

    # --- DEPLACEMENT DE LA COLONNE SEASON ---
    cols = df_final.columns.tolist()

    if 'Div' in cols and 'Season' in cols:
        # On retire 'Season' de sa position actuelle
        cols.remove('Season')

        index_div = cols.index('Div')

        cols.insert(index_div + 1, 'Season')

        df_final = df_final[cols]
        print("Colonne 'Season' place a cote de 'Div'.")

    #Sauvegarde
    chemin_final = os.path.join(dossier_sortie, nom_fichier_final)
    df_final.to_csv(chemin_final, index=False)

    print("-" * 30)
    print("TERMINÉ.")
    print(f"Fichier sauvegarde ici : {chemin_final}")
    print(f"Dimensions : {df_final.shape}")
    print("-" * 30)

else:
    print("Aucun fichier CSV trouve.")