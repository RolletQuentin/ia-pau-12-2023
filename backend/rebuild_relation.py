from projet_projet import recommandation_all_projets
from pyairtable import Api
from settings import base_id,api_keys,tables_id


api = Api(api_keys)

def delete_put_all_relation(log):
    bdd_relation = api.table(base_id, tables_id["relation"])
    bdd_relation.batch_delete([relation['id'] for relation in bdd_relation.all()])
    recommandation_all_projets(log)

delete_put_all_relation(True)