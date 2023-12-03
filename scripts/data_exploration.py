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

    # Trouvez la première et la dernière heure dans vos données
    min_hour = data['heure'].min()
    max_hour = data['heure'].max()

    # Calculez la plage de temps en minutes entre la première et la dernière heure
    time_range = pd.date_range(start=min_hour, end=max_hour, freq='T')

    # Créez un graphique temporel de l'activité avec des barres de 1 minute
    plt.figure(figsize=(12, 6))

    # Extraitz les minutes de la colonne 'heure' pour les utiliser en tant qu'abscisses
    minutes = data['heure'].dt.minute

    # Comptez le nombre d'activités pour chaque minute
    activity_count = minutes.value_counts().sort_index()

    # Créez le graphique en barres
    activity_count.plot(kind='bar', width=0.8, color='blue')

    plt.xlabel('Heure')
    plt.ylabel('Activité')
    plt.title('Activité au fil des minutes')

    # Utilisez la plage de temps en minutes pour les abscisses
    plt.xticks(range(len(time_range)), [time.strftime('%H:%M') for time in time_range], rotation=45)
    plt.grid(axis='y')

    plt.show()
