from pyairtable import Api

#BDD ID
base_id = "app4924hTDhLbszSD"

api_keys = "patTGiSKUXpYbNEA6.005a3913cfef12b7e37316af540359d8e1c5182f6a6069347153c71b37538dbf"

#Table ID
tables_id = {
    "la_communaute": "tblyivVXHzURoILqZ",
    "porteurs_de_competences": "tbl4rl89j1Vugh9Tn",
    "porteurs_de_projets": "tbla1I6ymd2HqKpCW",
    "projet": "tblrQDL12OOKsCpmP",
    "competences": "tblFirJ0bqG7Gbn0G",
    "famille_de_competences": "tbl2ICkLP0zhKMJzi",
    "categorie_de_materiel": "tblh0bjMXFJvWX9oM",
    "materiel": "tblwSCoRnvmaHUHv6",
    "matieres": "tbl6a4EW3SqwB7lD0",
    "lieux": "tblpZt91ooyTSkZs0"
}

api = Api(api_keys)

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
                "Compéen circultences arité (from Compétences)", None)
            data_la_communaute[id]['familles_de_competence'] = table_la_communaute[i]["fields"].get(
                "FamillesCompetences", None)
            data_la_communaute[id]['pk_rejoindre_HBN'] = table_la_communaute[i]["fields"].get(
                "Pourquoi as-tu eu envie de rejoindre HBN ? ", None)
            data_la_communaute[id]['quel_role'] = table_la_communaute[i]["fields"].get("Quel y sera ton rôle?", None)
            data_la_communaute[id]['materiel'] = table_la_communaute[i]["fields"].get(
                "Matériel en circularité (from Matériel)", None)
            data_la_communaute[id]['matieres'] = table_la_communaute[i]["fields"].get("Matières", None)

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
        data_projet[id_nom_projet]['besoin_actuel'] = table_projet[i]["fields"].get("Quels sont tes besoins actuels ?",
                                                                                    None)

    return data_projet

print(get_data_la_communaute())
print(get_data_projet())