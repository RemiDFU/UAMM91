import pandas as pd

def open_csv_file(file_path):
    try:
        # Utilisez pandas pour lire le fichier CSV
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'ouverture du fichier CSV : {str(e)}")
        return None

# Exemple d'utilisation
file_path = '/data/datasets/votre_fichier.csv'
data = open_csv_file(file_path)

if data is not None:
    # Maintenant, vous pouvez travailler avec les données dans 'data'
    print(data.head())  # Affiche les premières lignes du DataFrame
