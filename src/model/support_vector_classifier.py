import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Charger vos données en utilisant pandas
df = pd.read_csv("../../data/datasets/output_data_2023-11-29_19-05-17.csv")

# Séparez les caractéristiques (X) de la cible (y)
X = df.drop('heure', axis=1)  # Remplacez 'votre_colonne_cible' par le nom de votre colonne cible
y = df['niveau']

# Divisez les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créez un modèle SVM/SVC
model = SVC(kernel='linear')  # Vous pouvez choisir différents noyaux (linear, rbf, etc.)

# Entraînez le modèle sur l'ensemble d'entraînement
model.fit(X_train, y_train)

# Faites des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluez les performances du modèle
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Précision du modèle : ", accuracy)
print("Rapport de classification : \n", report)
