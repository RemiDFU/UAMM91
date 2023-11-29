import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

from sklearn import tree
import matplotlib.pyplot as plt

# Chargement des données dans un DataFrame
data = pd.read_csv("../../data/datasets/output_data_2023-11-29_19-05-17.csv", delimiter=",")


print(data.head())
print(data.shape)

# Vérifier s'il y a des valeurs manquantes dans chaque colonne
missing_values = data.isnull().sum()
print("valeurs manquantes :\n", missing_values)

# Extraction des caractéristiques (features) et des étiquettes (labels)
X = data.drop(["heure", "tache"], axis=1)  # Exclure les colonnes "heure" et "tache" comme caractéristiques
y = data["tache"]  # Utiliser uniquement la colonne "tache" comme étiquette

# Convertir les valeurs de la colonne "niveau" en valeurs numériques
niveau_mapping = {"ERROR": 1}  # Remplacez "ERROR" par une valeur numérique appropriée si nécessaire
X["niveau"] = X["niveau"].map(niveau_mapping)

# Encodage one-hot des variables catégorielles
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X)

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Création du modèle d'arbre de décision avec 'niveau' comme premier nœud racine
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

# Visualiser l'arbre de décision avec 'niveau' comme nœud racine et 'tache' comme second nœud
# Noms des caractéristiques (features) et des classes
feature_names = X.columns.tolist()
class_names = y.unique().tolist()

n_nodes = model.tree_.node_count
children_left = model.tree_.children_left
children_right = model.tree_.children_right
feature = model.tree_.feature
threshold = model.tree_.threshold

print("Nombre de noeuds:", n_nodes)
print("children_left:", children_left)
print("children_right:", children_right)
print("feature:", feature)
print("threshold", threshold)

print("classes:", class_names)

# Visualisation de l'arbre de décision
plt.figure(figsize=(20, 12))
tree.plot_tree(model, feature_names=feature_names, class_names=None, filled=True)
plt.show()

# Obtenir les valeurs des feuilles de l'arbre de décision
leaf_values = model.tree_.value  # Les valeurs de chaque feuille

# Obtenir le nombre de classes à partir de la forme des valeurs des feuilles
num_classes = leaf_values.shape[2]

# Créer un DataFrame pour afficher les valeurs des feuilles
leaf_df = pd.DataFrame(columns=range(num_classes), data=leaf_values.reshape(-1, num_classes))

# Ajouter une colonne pour le nombre total d'échantillons dans chaque feuille
leaf_df['Total Samples'] = leaf_df.sum(axis=1)

# Afficher le DataFrame avec les valeurs des feuilles
print("\nFeuilles de l'arbre de décision avec les valeurs de chaque classe :\n")
print(leaf_df)