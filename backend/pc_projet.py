import fasttext

from airtable_api import get_data_la_communaute
from airtable_api import get_data_projet
from model import similarity_score_texte
from geopy.geocoders import Nominatim  # Distance entre deux code postaux
from geopy.distance import geodesic  # Distance entre deux code postaux
import settings
model_path = 'cc.fr.300.bin'

"""Doc
Code Postal <-> Code Postal
@param IdPC : Id d'un PC
@param ID_Projet : Id d'un projet
@return Note allant de 0 à 3 pts.
"""


def fc_proximite_geographique(IdPC, ID_Projet):
    try:
        if (data_la_communaute[IdPC]["code_postal"] is not None) and (data_projet[ID_Projet]["code_postal"] is not None):
            geolocator = Nominatim(user_agent="my_geocoder")
            location1 = geolocator.geocode(str(data_la_communaute[IdPC]["code_postal"]) + ", France")
            location2 = geolocator.geocode(str(data_projet[ID_Projet]["code_postal"]) + ", France")
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
description <-> pkRejoindre
@param IdPC : Id d'un PC
@param ID_Projet : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_pk_rejoindre(IdPC, ID_Projet, model):
    try:
        # On compare pourquoi rejoindre avec descrition

        PC_pk_rejoindre = data_la_communaute[IdPC]['pk_rejoindre_HBN']  # Char
        Projet_description = data_projet[ID_Projet]['description']  # Char

        similarity_score = 0

        if PC_pk_rejoindre != None:
            if Projet_description != None:
                actual_similarity_score = similarity_score_texte(PC_pk_rejoindre, Projet_description, model)
                if actual_similarity_score > similarity_score:
                    similarity_score = actual_similarity_score

        # On gère le cas ou on a pas trouvé de correlation a cause de l'absence de variables
        if similarity_score == 0:
            similarity_score = -1

        return similarity_score
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


"""Doc
Description & Besoin actuel <-> Competence cir & familles comp & quel_role
@param IdPC : Id d'un PC
@param ID_Projet : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_flux_competences(IdPC, ID_Projet, model):
    try:
        # On compare chaque compétence en circularité avec les besoins actuels du projet et la description.
        # Puis on compare chaque famille de compétence avec les besoins actuels du projet et la description.
        # On compare quel role avec besoin actuel et description.
        # On garde le meilleur.

        PC_competences_circularite = data_la_communaute[IdPC]['competences_en_circularite']  # Liste
        PC_familles_competences = data_la_communaute[IdPC]['familles_de_competence']  # Liste
        PC_quel_role = data_la_communaute[IdPC]['quel_role']  # Char
        Projet_besoins_actuels = data_projet[ID_Projet]['besoin_actuel']  # Char
        Projet_description = data_projet[ID_Projet]['description']  # Char

        similarity_score = 0

        if PC_competences_circularite != None:
            for competence in PC_competences_circularite:
                # Je regarde si le nouveau similarity_score > similarity_score et je le remplace si c'est le cas.
                if Projet_besoins_actuels != None:
                    actual_similarity_score = similarity_score_texte(competence, Projet_besoins_actuels, model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score
                if Projet_description != None:
                    actual_similarity_score = similarity_score_texte(competence, Projet_description, model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score

        if PC_familles_competences != None:
            for competence in PC_familles_competences:
                # Je regarde si le nouveau similarity_score > similarity_score et je le remplace si c'est le cas.
                if Projet_besoins_actuels != None:
                    actual_similarity_score = similarity_score_texte(competence, Projet_besoins_actuels, model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score
                if Projet_description != None:
                    actual_similarity_score = similarity_score_texte(competence, Projet_description, model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score

        if PC_quel_role != None:
            if Projet_besoins_actuels != None:
                actual_similarity_score = similarity_score_texte(PC_quel_role, Projet_besoins_actuels, model)
                if actual_similarity_score > similarity_score:
                    similarity_score = actual_similarity_score
            if Projet_description != None:
                actual_similarity_score = similarity_score_texte(PC_quel_role, Projet_description, model)
                if actual_similarity_score > similarity_score:
                    similarity_score = actual_similarity_score

        # On gère le cas ou on a pas trouvé de correlation a cause de l'absence de variables
        if similarity_score == 0:
            similarity_score = -1

        return similarity_score

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


"""Doc
 besoin_actuel <-> materiel
@param IdPC : Id d'un PC
@param ID_Projet : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_flux_materiel(IdPC, ID_Projet, model):
    try:
        # On compare chaque materiel en circularité avec les besoins actuels du projet. On garde la meilleure relation.

        PC_materiels = data_la_communaute[IdPC]['materiel']  # Liste
        Projet_besoins_actuels = data_projet[ID_Projet]['besoin_actuel']  # Char

        similarity_score = 0

        if PC_materiels != None:
            for materiel in PC_materiels:
                # Je regarde si le nouveau similarity_score > similarity_score et je le remplace si c'est le cas.
                if Projet_besoins_actuels != None:
                    actual_similarity_score = similarity_score_texte(materiel, Projet_besoins_actuels, model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score

        # On gère le cas ou on a pas trouvé de correlation a cause de l'absence de variables
        if similarity_score == 0:
            similarity_score = -1

        return similarity_score
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


"""Doc
matiere_ent & besoin_actuel <-> matiere
@param IdPC : Id d'un PC
@param ID_Projet : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_flux_matiere(IdPC, ID_Projet, model):
    try:

        # On compare chaque matière que possède le Porteur de compétence et la matière entrante du projet (celle dont il a besoin).
        # De plus on va comparer chaque matiere que possède le Porteur de compétence et les besoins du porteur de projet aucas où il n'aurait pas remplis la matière entrante.
        # On prend le meilleur résultat.
        PC_matieres = data_la_communaute[IdPC]['matieres']  # Liste
        Projet_matiere_entrante = data_projet[ID_Projet]['matières_entrantes']  # Char
        Projet_besoins_actuels = data_projet[ID_Projet]['besoin_actuel']  # Char

        similarity_score = -1

        if PC_matieres is not None:
            for matiere in PC_matieres:
                # Je regarde si le nouveau similarity_score > similarity_score et je le remplace si c'est le cas.
                if Projet_matiere_entrante is not None:
                    actual_similarity_score = similarity_score_texte(matiere, Projet_matiere_entrante, model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score
                # Je fais de même pour notre deuxième cas
                if Projet_besoins_actuels is not None:
                    actual_similarity_score = similarity_score_texte(matiere, Projet_besoins_actuels, model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score
        return similarity_score
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


"""Doc
Domaine activite <-> famaille Comp
@param IdPC : Id d'un PC
@param ID_Projet : Id d'un projet
@return note normalisé entre 0 et 1.
"""


def fc_champ_lexical(IdPC, ID_Projet, model):
    try:
        # On va analyser chaque famille de compétence du porteur de compétences avec chaque domaine d'activité du projet et garder la meilleure similarité.
        PC_familles_de_competences = data_la_communaute[IdPC]['familles_de_competence']  # Liste
        Projet_domaine_activite = data_projet[ID_Projet]['domaine_activite']  # Char
        similarity_score = 0

        if PC_familles_de_competences != None:
            for famille_de_competence in PC_familles_de_competences:
                if Projet_domaine_activite != None:
                    actual_similarity_score = similarity_score_texte(famille_de_competence, Projet_domaine_activite,
                                                                     model)
                    if actual_similarity_score > similarity_score:
                        similarity_score = actual_similarity_score

        # On gère le cas ou on a pas trouvé de correlation a cause de l'absence de variables
        if similarity_score == 0:
            similarity_score = -1

        return similarity_score
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return -1


data_la_communaute = get_data_la_communaute()
data_projet = get_data_projet()


def recommandatation_pc_projet(IdPC, ID_Projet, model):
    coef_proximite_geographique = fc_proximite_geographique(IdPC, ID_Projet)
    coef_interet = fc_pk_rejoindre(IdPC, ID_Projet, model)
    coef_flux_competence = fc_flux_competences(IdPC, ID_Projet, model)
    coef_flux_materiel = fc_flux_materiel(IdPC, ID_Projet, model)
    coef_flux_matiere = fc_flux_matiere(IdPC, ID_Projet, model)
    coef_champ_lexical = fc_champ_lexical(IdPC, ID_Projet, model)

    tot_poids = 0
    tot_coef = 0

    if coef_proximite_geographique != -1:
        tot_poids += settings.poids_pc_projet_proximite_geographique
        coef_proximite_geographique = coef_proximite_geographique /3
        tot_coef += coef_proximite_geographique * settings.poids_pc_projet_proximite_geographique
    if coef_interet != -1:
        tot_poids += settings.poids_pc_projet_interet
        tot_coef += coef_interet* settings.poids_pc_projet_interet
    if coef_flux_competence != -1:
        tot_poids += settings.poids_pc_projet_flux_competence
        tot_coef += coef_flux_competence * settings.poids_pc_projet_flux_competence
    if coef_flux_materiel != -1:
        tot_poids += settings.poids_pc_projet_flux_materiel
        tot_coef += coef_flux_materiel * settings.poids_pc_projet_flux_materiel
    if coef_flux_matiere != -1:
        tot_poids += settings.poids_pc_projet_flux_matiere
        tot_coef += coef_flux_matiere * settings.poids_pc_projet_flux_matiere
    if coef_champ_lexical != -1:
        tot_poids += settings.poids_pc_projet_champ_lexical
        tot_coef += coef_champ_lexical * settings.poids_pc_projet_champ_lexical

    coef = tot_coef / tot_poids

    res = {"coef": coef,
           "coef_proximite_geographique": str(coef_proximite_geographique),
           "coef_interet": str(coef_interet),
           "coef_flux_competence": str(coef_flux_competence),
           "coef_flux_materiel": str(coef_flux_materiel),
           "coef_flux_matiere": str(coef_flux_matiere),
           "coef_champ_lexical": str(coef_champ_lexical)
           }
    return res




def recommendatation_pc_all_projets(IdPC):
    model = fasttext.load_model(model_path)
    res = {}
    for key in data_projet.keys():
        res[key] = recommandatation_pc_projet(IdPC,key,model)
    del model
    return res

def recommendatation_projet_all_pc(ID_Projet):
    model = fasttext.load_model(model_path)
    res = {}
    for key in data_la_communaute.keys():
        res[key] = recommandatation_pc_projet(key,ID_Projet,model)
    del model
    return res

print(recommendatation_projet_all_pc('Gioia'))
