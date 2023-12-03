import pandas as pd

def open_csv_file(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'ouverture du fichier CSV : {str(e)}")
        return None
