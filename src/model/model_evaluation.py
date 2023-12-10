from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, confusion_matrix

def calculate_accuracy(y_true, y_pred):
    """Calcule et retourne la précision du modèle."""
    return accuracy_score(y_true, y_pred)

def calculate_recall(y_true, y_pred, average='macro'):
    """Calcule et retourne le rappel du modèle."""
    return recall_score(y_true, y_pred, average=average)

def calculate_precision(y_true, y_pred, average='macro'):
    """Calcule et retourne la précision du modèle."""
    return precision_score(y_true, y_pred, average=average)

def calculate_f1_score(y_true, y_pred, average='macro'):
    """Calcule et retourne le score F1 du modèle."""
    return f1_score(y_true, y_pred, average=average)

def get_confusion_matrix(y_true, y_pred):
    """Génère et retourne la matrice de confusion du modèle."""
    return confusion_matrix(y_true, y_pred)
