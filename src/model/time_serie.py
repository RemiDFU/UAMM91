import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Charger vos données en utilisant pandas
df = pd.read_csv("../../data/datasets/output_data_2023-11-29_19-05-17.csv")

# Assurez-vous que votre dataframe a une colonne de dates au format datetime
# Si ce n'est pas le cas, vous pouvez utiliser df['heure'] = pd.to_datetime(df['heure'])

# Créez un modèle ARIMA
model = ARIMA(df['niveau'], order=(1,1,1))  # Vous pouvez ajuster l'ordre (p,d,q) en fonction de vos données

# Ajustez le modèle aux données
model_fit = model.fit()

# Effectuez une prévision pour les prochaines n périodes (à adapter)
n = 10
forecast = model_fit.forecast(steps=n)

# Affichez le résultat de la prévision
print("Prévision ARIMA : ", forecast)

# Affichez le graphique des données originales et de la prévision
plt.figure(figsize=(12, 6))
plt.plot(df['heure'], df['niveau'], label='Données Originales', color='blue')
plt.plot(pd.date_range(start=df['heure'].max(), periods=n, freq='D'), forecast, label='Prévision ARIMA', color='red')
plt.xlabel('Date')
plt.ylabel('Valeur')
plt.legend()
plt.title('Prévision ARIMA')
plt.show()
