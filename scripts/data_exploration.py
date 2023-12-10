import matplotlib.pyplot as plt
import pandas as pd

# Fonction pour le diagramme à barres de la fréquence des niveaux d'information
def plot_info_frequency(data):
    info_counts = data['niveau'].value_counts()
    plt.bar(info_counts.index, info_counts.values)
    plt.xlabel('Niveau d\'information')
    plt.ylabel('Fréquence')
    plt.title('Fréquence des Niveaux d\'Information')
    plt.xticks(rotation=45)
    plt.show()

# Fonction pour le diagramme à secteurs de la répartition des tâches
def plot_task_distribution(data):
    task_counts = data['tache'].value_counts()
    plt.pie(task_counts.values, labels=task_counts.index, autopct='%1.1f%%')
    plt.title('Répartition des Tâches')
    plt.show()

# Fonction pour le graphique temporel de l'activité
def plot_temporal_activity(data):
    # Assurez-vous que la colonne 'heure' est de type datetime
    data['heure'] = pd.to_datetime(data['heure'])

    # Agrégation des données par tranche de 15 minutes
    data_aggregated = data.resample('15T', on='heure').count()  # '15T' pour 15 minutes

    # Créez un graphique temporel de l'activité avec des barres de 15 minutes
    plt.figure(figsize=(12, 6))

    # Tracer l'activité
    data_aggregated.plot(kind='bar', width=0.8, color='blue', legend=False)

    plt.xlabel('Heure')
    plt.ylabel('Activité')
    plt.title('Activité par Tranche de 15 Minutes')

    # Ajuster les étiquettes de l'axe des x pour la lisibilité
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    plt.show()


def display_log_statistics(data):

    # Nombre total de logs
    total_logs = len(data)
    print(f"Nombre total de logs : {total_logs}")

    error_logs = len(data[data['niveau'] == 'ERROR'])
    print(f"Nombre de logs avec le niveau 'ERROR' : {error_logs}")

    error_logs = len(data[data['niveau'] == 'INFO'])
    print(f"Nombre de logs avec le niveau 'INFO' : {error_logs}")

    error_logs = len(data[data['niveau'] == 'WARNING'])
    print(f"Nombre de logs avec le niveau 'WARNING' : {error_logs}")

    print("\nNombre de logs par tâche :")
    task_counts = data['tache'].value_counts()
    print(task_counts)
