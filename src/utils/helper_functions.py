import pandas as pd

def save_to_csv(dataframe, output_filename):
    """
    Sauvegarde un DataFrame pandas dans un fichier CSV.

    Args:
        dataframe (pd.DataFrame): Le DataFrame à sauvegarder.
        output_filename (str): Le nom du fichier CSV de sortie.
    """
    try:
        dataframe.to_csv(output_filename, index=False)
        print(f"Les données ont été sauvegardées dans {output_filename}")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la sauvegarde du fichier CSV : {str(e)}")
