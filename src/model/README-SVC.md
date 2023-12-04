# Modèle de Classification des Logs avec SVM

## Aperçu

Ce modèle de Support Vector Machine (SVM) classifie les niveaux de logs (INFO, WARNING, ERROR) dans un ensemble de données de logs. Ce processus est un exemple typique d'une tâche de classification supervisée en machine learning.

## Processus

### 1. Chargement des Données

- Les données sont chargées dans un DataFrame Pandas à partir d'un fichier CSV.
- Les données incluent des timestamps, des niveaux de log et d'autres informations pertinentes.

### 2. Encodage des Étiquettes

- La colonne `niveau` est transformée de valeurs catégorielles en valeurs numériques avec `LabelEncoder`.

### 3. Préparation des Caractéristiques et des Étiquettes

- Séparation des caractéristiques (`X`) et des étiquettes (`y`).
- Exclusion de la colonne `heure` et utilisation de `niveau` comme étiquette.

### 4. Prétraitement des Caractéristiques

- Transformation des colonnes catégorielles avec `OneHotEncoder` dans un `ColumnTransformer`.

### 5. Division des Données

- Division en ensembles d'entraînement et de test avec `train_test_split`.

### 6. Pipeline de Traitement et d'Apprentissage

- Création d'un pipeline avec `make_pipeline` incluant `ColumnTransformer`, `StandardScaler` et `SVC`.
- Utilisation de `StandardScaler` pour la mise à l'échelle des caractéristiques.
- Choix du SVM avec un noyau linéaire.

### 7. Entraînement du Modèle

- Entraînement sur l'ensemble d'entraînement.
- Le SVM cherche un hyperplan pour séparer les classes.

### 8. Prédiction et Évaluation

- Prédictions sur l'ensemble de test.
- Calcul de la précision et production d'un rapport de classification.

## Utilisation

Ce modèle peut être utilisé pour prédire les niveaux de log de nouvelles données non vues, ce qui est utile pour la surveillance automatique des systèmes et la détection précoce des problèmes.


