from datetime import datetime

import pandas as pd
import re
import matplotlib.pyplot as plt


logs = []

with open("../../data/rawData/worker-c382_21_11_2023.log", "r", encoding="utf-8") as file:
    #logs = file.readlines()[1130000:1140000]
    logs = file.readlines()[450000:550000]



df = pd.DataFrame(columns=['heure', 'niveau', 'tache'])

line_count = 0

for log in logs:
    line_count += 1
    # Extraction de l'heure
    heure = log[1:24]

    # Extraction du niveau d'information
    niveau_matches = re.findall(r": (.*?)/", log)
    print("niveau_matches:", niveau_matches)
    niveau = niveau_matches[0] if niveau_matches else "N/A"

    # Extraction du nom de la tâche
    tache_matches = re.findall(r"\](.*?)\[", log)
    tache = tache_matches[0] if tache_matches else "N/A"
    tache = tache.replace("Received task:", "")
    tache = tache.replace("Task", "")
    tache = tache.replace(" ", "")

    df = df.append({'heure': heure, 'niveau': niveau, 'tache': tache}, ignore_index=True)


unique_niveaux = df['niveau'].unique()
print(f"Ligne {line_count} traitée")
print("Différents types de niveau:", unique_niveaux)


# Compter le nombre d'occurrences pour chaque niveau d'information
info_counts = df['niveau'].value_counts(normalize=True, dropna=False)

# Compter le nombre d'occurrences pour chaque tâche
task_counts = df['tache'].value_counts()


################################################
# Filtered
filtered_df = df[df['tache'].str.strip() != 'scheduled_notification_job']
info_counts_filtered = filtered_df['tache'].value_counts()
print(filtered_df)

plt.bar(info_counts_filtered.index, info_counts_filtered.values)
plt.xlabel('Tâches')
plt.ylabel('Fréquence')
plt.title('Distribution des types de tâches')
plt.show()


plt.pie(info_counts_filtered.values, labels=info_counts_filtered.index, autopct='%1.1f%%')
plt.title('Répartition des tâches')
plt.show()



plt.bar(info_counts_filtered.index, info_counts_filtered.values)
plt.xlabel('Tâche')
plt.ylabel('Fréquence')
plt.title('Fréquence des tâches')
plt.xticks(rotation=90)
plt.show()

# Compter le nombre de lignes pour chaque niveau
niveau_counts = df['niveau'].value_counts()

print(niveau_counts)


# Compter le nombre d'occurrences pour chaque tâche
filtered_df = df[df['tache'].str.strip() != 'scheduled_notification_job']
info_counts_filtered = filtered_df['tache'].value_counts()

# Calculer le pourcentage pour chaque tâche
task_percentages = (info_counts_filtered / len(df)) * 100

# Créer un DataFrame à partir des pourcentages
task_table = pd.DataFrame({'Tâche': task_percentages.index, 'Pourcentage': task_percentages.values})

# Trier le DataFrame par ordre décroissant de pourcentage
task_table = task_table.sort_values('Pourcentage', ascending=False)

# Afficher le tableau de répartition des tâches
print(task_table)

current_datetime = datetime.now()

# Formater la date et l'heure pour le nom du fichier
formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

# Nom du fichier CSV avec date et heure
output_filename = f"output_data_{formatted_datetime}.csv"

# Sauvegarder le DataFrame dans un fichier CSV
df.to_csv(path_or_buf="../../data/datasets/"f"{output_filename}", index=False)
