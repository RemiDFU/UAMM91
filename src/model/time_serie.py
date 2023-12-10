import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt

def forecast_log_levels(csv_path, column_name, arima_order, forecast_steps):
    """
    Fonction pour prévoir les niveaux de logs en utilisant un modèle ARIMA.

    Args:
    - csv_path (str): Chemin vers le fichier CSV contenant les données de logs.
    - column_name (str): Nom de la colonne des niveaux de log à analyser.
    - arima_order (tuple): Un tuple (p, d, q) pour les paramètres du modèle ARIMA.
    - forecast_steps (int): Nombre de pas de temps pour lesquels faire la prévision.

    Returns:
    - Affiche un graphique de la série temporelle et des prévisions.
    """
    # Charger les données
    df = pd.read_csv(csv_path, delimiter=",")
    df['heure'] = pd.to_datetime(df['heure'])
    df.set_index('heure', inplace=True)

    # Analyser la fréquence des logs spécifiés par heure
    df_filtered = df[df['niveau'] == column_name].resample('H').size()

    # Afficher les graphiques ACF et PACF
    # TODO

    # Modèle ARIMA
    model = ARIMA(df_filtered, order=arima_order)
    model_fit = model.fit()

    # Prévisions
    predictions = model_fit.forecast(steps=forecast_steps)

    # Visualisation
    plt.figure(figsize=(10,6))
    plt.plot(df_filtered, label=f'Nombre de logs {column_name} par heure')
    plt.plot(predictions, label='Prévisions', color='red')
    plt.title(f'Prévisions du Nombre de Logs {column_name}')
    plt.xlabel('Heure')
    plt.ylabel('Nombre de Logs')
    plt.legend()
    plt.show()

# RUN func
forecast_log_levels("../../data/datasets/output_data_2023-12-10_17-06-11.csv", "ERROR", (10, 5, 10), 2)
