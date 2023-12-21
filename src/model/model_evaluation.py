from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns



def calculate_accuracy(y_true, y_pred):
    return accuracy_score(y_true, y_pred)


def calculate_recall(y_true, y_pred, average='macro'):
    return recall_score(y_true, y_pred, average=average)


def calculate_precision(y_true, y_pred):
    return precision_score(y_true, y_pred, average='macro', zero_division=1)


def calculate_f1_score(y_true, y_pred, average='macro'):
    """Calcule et retourne le score F1 du modèle."""
    return f1_score(y_true, y_pred, average=average)


def get_confusion_matrix(y_true, y_pred):
    """Génère et retourne la matrice de confusion du modèle."""
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Prédictions")
    plt.ylabel("Vraies valeurs")
    plt.title("Matrice de Confusion")
    plt.show()
    return confusion_matrix(y_true, y_pred)
