from airtable_api import get_data_projet

import settings

import numpy as np

from geopy.geocoders import Nominatim  # Distance entre deux code postaux
from geopy.distance import geodesic  # Distance entre deux code postaux

from model import get_text_vector
from model import similarity_score_texte

"""Doc
Code Postal <-> Code Postal
@param ZIP_CODE_1 : code postal
@param ZIP_CODE_2 : code postal
@return Note allant de 0 à 3 pts.
"""


def fc_proximite_geographique(ZIP_CODE_1, ZIP_CODE_2):
    try:
        geolocator = Nominatim(user_agent="my_geocoder")

        location1 = geolocator.geocode(str(ZIP_CODE_1) + ", France")
        location2 = geolocator.geocode(str(ZIP_CODE_2) + ", France")

        distance = geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km

        if distance < 50:
            note = 3
        elif distance < 100:
            note = 2
        elif distance < 150:
            note = 1
        else:
            note = 0

        return note

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return 0


"""Doc
description <-> description
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_champ_lexical(ID1, ID2):
    try:
        # On compare les description de projets
        # On récupère nos données
        Projet1_description = data_projet[ID1]['description']  # Char
        Projet2_description = data_projet[ID2]['description']  # Char
        similarity_score = 0

        if Projet1_description != None and Projet2_description != None:
            similarity_score = similarity_score_texte(Projet1_description, Projet2_description)

        return similarity_score
    except Exception as e:
        return f"Une erreur s'est produite : {e}"


"""Doc
matières_entrantes <-> coproduits <-> besoin_actuel
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_flux_matiere(ID1, ID2):
    try:
        # 1. On compare si les matière entrante d'un projet correspondent aux matières sortante d'un autre et réciproquement.
        # 2. On compare les besoins d'un projet et les matières sortante d'un autre et réciproquement
        # On prend le maximum
        Projet1_matiere_entrante = data_projet[ID1]['matières_entrantes']  # Char
        Projet2_matiere_entrante = data_projet[ID2]['matières_entrantes']  # Char

        Projet1_matiere_sortante = data_projet[ID1]['coproduits']  # Char
        Projet2_matiere_sortante = data_projet[ID2]['coproduits']  # Char

        Projet1_besoins_actuels = data_projet[ID1]['besoin_actuel']  # Char
        Projet2_besoins_actuels = data_projet[ID2]['besoin_actuel']  # Char

        similarity_score = 0

        # 1.
        if Projet1_matiere_entrante != None and Projet2_matiere_sortante != None:
            actual_similarity_score = similarity_score_texte(Projet1_matiere_entrante, Projet2_matiere_sortante)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score
        if Projet2_matiere_entrante != None and Projet1_matiere_sortante != None:
            actual_similarity_score = similarity_score_texte(Projet2_matiere_entrante, Projet1_matiere_sortante)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score

        # 2.
        if Projet1_besoins_actuels != None and Projet2_matiere_sortante != None:
            actual_similarity_score = similarity_score_texte(Projet1_besoins_actuels, Projet2_matiere_sortante)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score
        if Projet2_besoins_actuels != None and Projet1_matiere_sortante != None:
            actual_similarity_score = similarity_score_texte(Projet2_besoins_actuels, Projet1_matiere_sortante)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score

        return similarity_score
    except Exception as e:
        return f"Une erreur s'est produite : {e}"


"""Doc
domaine-activite <-> domaine-activite 
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_flux_competences(ID1, ID2):
    try:
        # On compare les domaines d'activités des projets
        Projet1_domaine_activite = data_projet[ID1]['domaine_activite']  # Char
        Projet2_domaine_activite = data_projet[ID2]['domaine_activite']  # Char

        similarity_score = 0

        if Projet1_domaine_activite != None and Projet2_domaine_activite != None:
            similarity_score = similarity_score_texte(Projet1_domaine_activite, Projet2_domaine_activite)

        return similarity_score
    except Exception as e:
        return f"Une erreur s'est produite : {e}"


"""Doc
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return Note allant de 0 à 3 pts.
"""


def fc_domaine_application(ID1, ID2):
    try:
        # On compte les mêmes occurences des "ODD Fixé par l'ONU" des deux projets.
        occurence = 0

        # On récupère les listes de mot de chaque projet
        odd_projet1 = data_projet[ID1]['ODD']
        odd_projet2 = data_projet[ID2]['ODD']

        if odd_projet1 != None and odd_projet2 != None:
            # On parcourt nos listes de mots et compte les occurences
            for odd_p1 in odd_projet1:
                for odd_p2 in odd_projet2:
                    if odd_p1 == odd_p2:
                        occurence += 1

        # On défini la note
        if occurence >= 3:
            note = 3
        elif occurence == 2:
            note = 2
        elif occurence == 1:
            note = 1
        else:
            note = 0

        return note
    except Exception as e:
        return f"Une erreur s'est produite : {e}"


# Test Projet <-> Projet
"""
print(fc_proximite_geographique(10001, 11000))
print(fc_champ_lexical('ERRO ETXEA', 'Ekohameau'))
print(fc_champ_lexical('Ekohameau', 'ERRO ETXEA'))
print(fc_flux_matiere('ERRO ETXEA', 'Ekohameau'))
print(fc_flux_matiere('Ekohameau', 'ERRO ETXEA'))
print(fc_flux_competences('ERRO ETXEA', 'Ekohameau'))
print(fc_flux_competences('Ekohameau', 'ERRO ETXEA'))
print(fc_domaine_application('ERRO ETXEA', 'EKOBESTA'))
"""

data_projet = get_data_projet()


def recommandation_projet_projet(ID1, ID2):
    coef_proximite_geographique = fc_proximite_geographique(data_projet[ID1]["code_postal"], data_projet[ID2][
        "code_postal"]) * settings.poids_domain_application / 3
    coef_champ_lexical = fc_champ_lexical(ID1, ID2) * settings.poids_champ_lexical
    coef_flux_matiere = fc_flux_matiere(ID1, ID2) * settings.poids_proximite_geographique
    coef_flux_competence = fc_flux_competences(ID1, ID2) * settings.poids_flux_matiere / 3
    coef_domain_application = fc_domaine_application(ID1, ID2) * settings.poids_flux_competence
