import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from model_evaluation import calculate_accuracy, calculate_recall, calculate_precision, calculate_f1_score, get_confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE
from sklearn import tree
import matplotlib.pyplot as plt

# Chargement des données
data = pd.read_csv("../../data/datasets/output_data_2023-12-10_17-06-11.csv", delimiter=",")
print(data.head())
print(data.shape)

# Vérifier s'il y a des valeurs manquantes dans chaque colonne
missing_values = data.isnull().sum()
print("valeurs manquantes :\n", missing_values)

# Prétraitement des données
X = data.drop(["heure", "tache"], axis=1)
y = data["tache"]
niveau_mapping = {"INFO": 0, "WARNING": 1, "ERROR": 2}
X["niveau"] = X["niveau"].map(niveau_mapping)

# Encodage one-hot
encoder = OneHotEncoder()
X_encoded = encoder.fit_transform(X).toarray()
feature_names = encoder.get_feature_names_out(input_features=X.columns)

# Suréchantillonnage avec SMOTE
smote = SMOTE(k_neighbors=min(2, y.value_counts().min() - 1))
X_resampled, y_resampled = smote.fit_resample(X_encoded, y)

# Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

# Création et entraînement du modèle d'arbre de décision
model = DecisionTreeClassifier(max_depth=3, criterion='gini', class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Compter le nombre de classes
class_counts = data["tache"].value_counts()

# Afficher le nombre de classes
print("Nombre de classes :", len(class_counts))
print(class_counts)

# Noms des caractéristiques (features) et des classes
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



# Prédictions et évaluation
y_pred = model.predict(X_test)

print("Accuracy:", calculate_accuracy(y_test, y_pred))
print("Recall:", calculate_recall(y_test, y_pred))
print("Precision:", calculate_precision(y_test, y_pred))
print("F1 Score:", calculate_f1_score(y_test, y_pred))
print("Confusion Matrix:\n", get_confusion_matrix(y_test, y_pred))

# Visualiser l'arbre de décision
plt.figure(figsize=(20, 12))
tree.plot_tree(model, feature_names=feature_names, filled=True)
plt.show()
