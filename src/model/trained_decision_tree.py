import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
from sklearn.preprocessing import OneHotEncoder
from imblearn.over_sampling import SMOTE
from sklearn import tree
import matplotlib.pyplot as plt

# Chargement des données
data = pd.read_csv("../../data/datasets/output_data_2023-12-10_17-06-11.csv", delimiter=",")

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
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Création et entraînement du modèle d'arbre de décision
model = DecisionTreeClassifier(max_depth=3, criterion='gini', class_weight='balanced', random_state=42)
model.fit(X_train, y_train)

# Prédictions et évaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, average='macro')
precision = precision_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')
conf_matrix = confusion_matrix(y_test, y_pred)

# Affichage des résultats
print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1 Score:", f1)
print("Confusion Matrix:\n", conf_matrix)

# Visualiser l'arbre de décision
plt.figure(figsize=(20, 12))
tree.plot_tree(model, feature_names=feature_names, filled=True)
plt.show()
