import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn import tree
import matplotlib.pyplot as plt
from model_evaluation import calculate_accuracy, calculate_recall, calculate_precision, calculate_f1_score, get_confusion_matrix

# Chargement des données dans un DataFrame
data = pd.read_csv("../../data/datasets/output_data_2023-12-10_17-06-11.csv", delimiter=",")

print(data.head())
print(data.shape)

# Vérifier s'il y a des valeurs manquantes dans chaque colonne
missing_values = data.isnull().sum()
print("valeurs manquantes :\n", missing_values)

# Extraction des caractéristiques (features) et des étiquettes (labels)
X = data.drop(["heure", "tache"], axis=1)  # Exclure les colonnes "heure" et "tache" comme caractéristiques
y = data["tache"]  # Utiliser uniquement la colonne "tache" comme étiquette

# Convertir les valeurs de la colonne "niveau" en valeurs numériques
niveau_mapping = {"INFO": 0, "WARNING": 1, "ERROR": 2}
X["niveau"] = X["niveau"].map(niveau_mapping)

# Encodage one-hot des variables catégorielles
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X).toarray()
feature_names = encoder.get_feature_names_out(input_features=X.columns)

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Création du modèle d'arbre de décision
model = DecisionTreeClassifier(max_depth=3, criterion='gini', random_state=42)

# Entraînement du modèle
model.fit(X_train, y_train)

# Prédictions sur les données de test
y_pred = model.predict(X_test)

# Évaluation de la performance du modèle
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Compter le nombre de classes
class_counts = data["tache"].value_counts()

# Afficher le nombre de classes
print("Nombre de classes :", len(class_counts))
print(class_counts)

# Visualiser l'arbre de décision
plt.figure(figsize=(20, 12))
tree.plot_tree(model, feature_names=feature_names, filled=True)
plt.show()


# Calcul des métriques d'évaluation
accuracy = calculate_accuracy(y_test, y_pred)
recall = calculate_recall(y_test, y_pred)
precision = calculate_precision(y_test, y_pred)
f1 = calculate_f1_score(y_test, y_pred)
conf_matrix = get_confusion_matrix(y_test, y_pred)

# Affichage des résultats
print("Accuracy on Test Set:", accuracy)
print("Recall on Test Set:", recall)
print("Precision on Test Set:", precision)
print("F1 Score on Test Set:", f1)
print("Confusion Matrix on Test Set:\n", conf_matrix)
