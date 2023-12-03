import fasttext
from airtable_api import get_data_projet
import settings
from geopy.geocoders import Nominatim  # Distance entre deux code postaux
from geopy.distance import geodesic  # Distance entre deux code postaux
from airtable_api import get_projets
from airtable_api import put_new_relation
from model import similarity_score_texte


model_path = 'cc.fr.50.bin'

"""Doc
Code Postal <-> Code Postal
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return Note allant de 0 à 3 pts.
"""


def fc_proximite_geographique(ID1, ID2):
    try:
        if (data_projet[ID1]["code_postal"] is not None) and (data_projet[ID2]["code_postal"] is not None):
            geolocator = Nominatim(user_agent="my_geocoder")

            location1 = geolocator.geocode(str(data_projet[ID1]["code_postal"]) + ", France")
            location2 = geolocator.geocode(str(data_projet[ID2]["code_postal"]) + ", France")

            distance = geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).km

            if distance < 50:
                note = 3
            elif distance < 100:
                note = 2
            elif distance < 150:
                note = 1
            else:
                note = 0
        else:
            note = -1
        return note

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


"""Doc
description <-> description
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_champ_lexical(ID1, ID2, model):
    try:
        # On compare les description de projets
        # On récupère nos données
        Projet1_description = data_projet[ID1]['description']  # Char
        Projet2_description = data_projet[ID2]['description']  # Char
        similarity_score = 0

        if Projet1_description is not None and Projet2_description is not None:
            similarity_score = similarity_score_texte(Projet1_description, Projet2_description, model)
        else:
            similarity_score = -1
        return similarity_score
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


"""Doc
matières_entrantes <-> coproduits <-> besoin_actuel
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_flux_matiere(ID1, ID2, model):
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

        similarity_score = -1

        # 1.
        if Projet1_matiere_entrante is not None and Projet2_matiere_sortante is not None:
            actual_similarity_score = similarity_score_texte(Projet1_matiere_entrante, Projet2_matiere_sortante,model)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score
        if Projet2_matiere_entrante is not None and Projet1_matiere_sortante is not None:
            actual_similarity_score = similarity_score_texte(Projet2_matiere_entrante, Projet1_matiere_sortante,model)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score

        # 2.
        if Projet1_besoins_actuels is not None and Projet2_matiere_sortante != None:
            actual_similarity_score = similarity_score_texte(Projet1_besoins_actuels, Projet2_matiere_sortante, model)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score
        if Projet2_besoins_actuels is not None and Projet1_matiere_sortante is not None:
            actual_similarity_score = similarity_score_texte(Projet2_besoins_actuels, Projet1_matiere_sortante, model)
            if actual_similarity_score > similarity_score:
                similarity_score = actual_similarity_score

        return similarity_score
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


"""Doc
domaine-activite <-> domaine-activite 
@param ID1 : Id d'un projet
@param ID2 : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_flux_competences(ID1, ID2, model):
    try:
        # On compare les domaines d'activités des projets
        Projet1_domaine_activite = data_projet[ID1]['domaine_activite']  # Char
        Projet2_domaine_activite = data_projet[ID2]['domaine_activite']  # Char

        similarity_score = 0

        if Projet1_domaine_activite is not None and Projet2_domaine_activite is not None:
            similarity_score = similarity_score_texte(Projet1_domaine_activite, Projet2_domaine_activite, model)
        else:
            similarity_score = -1
        return similarity_score
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


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

        if odd_projet1 is not None and odd_projet2 is not None:
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
        else:
            note = -1

        return note
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


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

def recommandation_projet_projet(ID1, ID2, model):
    coef_proximite_geographique = fc_proximite_geographique(ID1,ID2)
    coef_champ_lexical = fc_champ_lexical(ID1, ID2, model)
    coef_flux_matiere = fc_flux_matiere(ID1, ID2, model)
    coef_flux_competence = fc_flux_competences(ID1, ID2, model)
    coef_domain_application = fc_domaine_application(ID1, ID2)

    tot_poids = 0
    tot_coef = 0
    if coef_proximite_geographique != -1:
        tot_poids += settings.poids_projet_projet_proximite_geographique
        coef_proximite_geographique = coef_proximite_geographique /3
        tot_coef += coef_proximite_geographique * settings.poids_projet_projet_proximite_geographique
    if coef_champ_lexical != -1:
        tot_poids += settings.poids_projet_projet_champ_lexical
        tot_coef += coef_champ_lexical * settings.poids_projet_projet_champ_lexical
    if coef_flux_matiere != -1:
        tot_poids += settings.poids_projet_projet_flux_matiere
        tot_coef += coef_flux_matiere * settings.poids_projet_projet_flux_matiere
    if coef_flux_competence != -1:
        tot_poids += settings.poids_projet_projet_flux_competence
        tot_coef += coef_flux_competence * settings.poids_projet_projet_flux_competence
    if coef_domain_application != -1:
        tot_poids += settings.poids_projet_projet_domain_application
        coef_domain_application = coef_domain_application /3
        tot_coef += coef_domain_application * settings.poids_projet_projet_domain_application

    coef = tot_coef / tot_poids

    res = {"coef": coef,
           "source": str(ID1),
           "cible": str(ID2),
           "coef_proximite_geographique": str(coef_proximite_geographique),
           "coef_champ_lexical": str(coef_champ_lexical),
           "coef_flux_matiere": str(coef_flux_matiere),
           "coef_flux_competence": str(coef_flux_competence),
           "coef_domain_application": str(coef_domain_application)
           }
    return res

def recommandation_projet_all_projets(ID):
    model = fasttext.load_model(model_path)
    res = []
    for key in data_projet.keys():
        if key != ID:
            res.append(recommandation_projet_projet(ID,key, model))
    put_new_relation(res)
    del model

def recommandation_all_projets(log=False):
    model = fasttext.load_model(model_path)
    res = []
    key_checked = []
    for key1 in data_projet.keys():  # Itération à travers les clés du dictionnaire
        for key2 in key_checked:
            res.append(recommandation_projet_projet(key1, key2, model))
        key_checked.append(key1)
        if log:
            print(len(key_checked))
    put_new_relation(res)
    del model

def recommandation_projet_allreco_projets(ID_Projet):
    data_projets = get_projets()
    model = fasttext.load_model(model_path)
    res = {}
    for key in data_projet.keys():
        res[key] = recommandation_projet_projet(key, ID_Projet, model)
    del model
    for projet in data_projets:
        projet["recommendation"] = res[projet["Nom du Projet"]]
    return sorted(data_projets, key=lambda x: x['recommendation']['coef'], reverse=True)


