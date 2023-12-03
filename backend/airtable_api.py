from pyairtable import Api
from settings import base_id,api_keys,tables_id


api = Api(api_keys)


def get_user(id):
    bdd_la_communaute = api.table(base_id, tables_id["la_communaute"])
    table_la_communaute = bdd_la_communaute.all()

    for i in range(len(table_la_communaute)):
        if table_la_communaute[i]["fields"]["ID"] == id:
            return table_la_communaute[i]["fields"]

    return { "ID": id, 'error': "inconnue" }

def get_data_la_communaute():
    bdd_la_communaute = api.table(base_id, tables_id["la_communaute"])
    table_la_communaute = bdd_la_communaute.all()

    data_la_communaute = {}

    for i in range(len(table_la_communaute)):
        if ('Adhérent Oui/Non/En attente' in table_la_communaute[i]["fields"]) and (
                table_la_communaute[i]["fields"]['Adhérent Oui/Non/En attente'] == "Oui"):
            id = table_la_communaute[i]["fields"]["ID"]

            if id not in data_la_communaute:
                data_la_communaute[id] = {}

            data_la_communaute[id]['code_postal'] = table_la_communaute[i]["fields"].get("Code postal", None)
            data_la_communaute[id]['competences_en_circularite'] = table_la_communaute[i]["fields"].get(
                "Compétences en circularité (from Compétences)", None)
            data_la_communaute[id]['familles_de_competence'] = table_la_communaute[i]["fields"].get(
                "FamillesCompetences", None)
            data_la_communaute[id]['pk_rejoindre_HBN'] = table_la_communaute[i]["fields"].get(
                "Pourquoi as-tu eu envie de rejoindre HBN ? ", None)
            data_la_communaute[id]['quel_role'] = table_la_communaute[i]["fields"].get("Quel y sera ton rôle?", None)
            data_la_communaute[id]['materiel'] = table_la_communaute[i]["fields"].get(
                "Matériel en circularité (from Matériel)", None)
            data_la_communaute[id]['matieres'] = table_la_communaute[i]["fields"].get("Matières", None)

            if data_la_communaute[id]['familles_de_competence'] is not None:
                data_la_communaute[id]['familles_de_competence'] = data_la_communaute[id][
                    'familles_de_competence'].split("\n")

            if data_la_communaute[id]['materiel'] is not None:
                data_la_communaute[id]['materiel'] = data_la_communaute[id]['materiel'].split(",")

            if data_la_communaute[id]['competences_en_circularite'] is not None:
                data_la_communaute[id]['competences_en_circularite'] = data_la_communaute[id]['competences_en_circularite'].split(",")

    return data_la_communaute

def get_data_projet():
    bdd_projet = api.table(base_id, tables_id["projet"])
    table_projet = bdd_projet.all()
    data_projet = {}

    for i in range(len(table_projet)):
        id_nom_projet = table_projet[i]["fields"]["Nom du Projet"]

        if id_nom_projet not in data_projet:
            data_projet[id_nom_projet] = {}

        data_projet[id_nom_projet]['code_postal'] = table_projet[i]["fields"].get("Code postal", None)
        data_projet[id_nom_projet]['description'] = table_projet[i]["fields"].get("Description du projet", None)
        data_projet[id_nom_projet]['matières_entrantes'] = table_projet[i]["fields"].get("Matières entrantes", None)
        data_projet[id_nom_projet]['domaine_activite'] = table_projet[i]["fields"].get("Domaine d'activité", None)
        data_projet[id_nom_projet]['coproduits'] = table_projet[i]["fields"].get("Coproduits", None)
        data_projet[id_nom_projet]['ODD'] = table_projet[i]["fields"].get("ODD fixé par l'ONU", None)
        data_projet[id_nom_projet]['besoin_actuel'] = table_projet[i]["fields"].get("Quels sont tes besoins actuels ?",None)

        if data_projet[id_nom_projet]['ODD'] is not None:
            data_projet[id_nom_projet]['ODD'] = data_projet[id_nom_projet]['ODD'].split(",")

    return data_projet

def get_data_projet_affichage():
    data_projet_affichage = {}
    bdd_projet = api.table(base_id, tables_id["projet"])
    table_projet = bdd_projet.all()
    nodes = []
    for i in range(len(table_projet)):
        nodes.append(table_projet[i]["fields"])

    bdd_edges = api.table(base_id, tables_id["relation"])
    table_edges = bdd_edges.all()
    edges = []
    for i in range(len(table_edges)):
        edges.append(table_edges[i]["fields"])
    data_projet_affichage["nodes"] = nodes
    data_projet_affichage["edges"] = edges

    return data_projet_affichage

def put_new_relation(data):
    bdd_relation = api.table(base_id, tables_id["relation"])
    bdd_relation.batch_create(data)

def put_new_project(data):
    bdd_projet = api.table(base_id, tables_id["projet"])
    bdd_projet.create({'Nom du Projet': data.nom_du_projet,
                        'Description du projet': data.description_du_projet,
                        'Quels sont tes besoins actuels ?': data.besoins_actuels,
                        "Domaine d'activité": data.domaine_activite,
                        "Maturité du projet": data.maturite_du_projet,
                        "Lieu du projet": data.lieu_du_projet,
                        "Code postal": int(data.code_postal),
                        "Code postal + ville": data.lieu_du_projet + data.code_postal,
                        "ODD fixé par l'ONU": ', '.join(data.odd),
                        "Matières entrantes": data.matieres_entrantes,
                        "Coproduits": data.coproduits
                       })