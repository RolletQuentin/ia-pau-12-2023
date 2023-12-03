
import numpy as np
# Chargement du modèle pré-entraîné


# Fonction pour obtenir le vecteur d'un texte
def get_text_vector(text, model):
    words = text.split()
    # Calcul de la moyenne des vecteurs de mots
    vector = sum(model.get_word_vector(word) for word in words) / len(words)
    return vector


# Fonction qui calcul la similarité sémentique entre deux texte. Renvoi une similarité entre 0 et 1.
def similarity_score_texte(texte1, texte2, model):
    # Obtenez les vecteurs des deux textes
    vector1 = get_text_vector(texte1, model)
    vector2 = get_text_vector(texte2, model)

    # Calcul du score de similarité cosinus entre les deux vecteurs
    similarity_score = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))

    return similarity_score
