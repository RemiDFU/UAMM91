import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import LabelEncoder

# Charger vos données en utilisant pandas
df = pd.read_csv("../../data/datasets/output_data_2023-12-03_16-53-42.csv")

# Si 'niveau' est une colonne catégorielle, encodez-la en valeurs numériques
label_encoder = LabelEncoder()
df['niveau'] = label_encoder.fit_transform(df['niveau'])

# Séparez les caractéristiques (X) de la cible (y)
# Assurez-vous de ne pas inclure des colonnes textuelles ou inappropriées
X = df.drop(['heure', 'niveau'], axis=1)
y = df['niveau']

# Prétraitement pour les colonnes catégorielles avec OneHotEncoder
categorical_features = X.select_dtypes(include=['object']).columns.tolist()
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), categorical_features),
    ],
    remainder='passthrough'  # Ce paramètre permet de conserver les autres colonnes non traitées
)

# Divisez les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créez un pipeline avec prétraitement et le modèle SVM
model = make_pipeline(
    preprocessor,
    StandardScaler(with_mean=False),  # SVM bénéficie de la mise à l'échelle des caractéristiques
    SVC(kernel='linear', random_state=42)
)

# Entraînez le modèle sur l'ensemble d'entraînement
model.fit(X_train, y_train)

# Faites des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Évaluez les performances du modèle
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Précision du modèle : ", accuracy)
print("Rapport de classification : \n", report)
