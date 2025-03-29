from app.Models.ListaModel import Lista, db
from app.Schemas.Schemas import ListaSchema
from app.Schemas.Schemas import MontagemSchema, ListaSchema
from app.datetime import datetime_sp_string

montagem_schema = MontagemSchema()

lista_schema = ListaSchema()
listas_schema = ListaSchema(many=True)

class ListaController:

    def __init__(self):
        pass

    def createLista(self, dados_nova_lista):
        try:
            nova_lista = lista_schema.load(dados_nova_lista, session=db.session)
            db.session.add(nova_lista)
            db.session.commit()
            # Retorne a instância (você pode usar o dump se preferir)
            return nova_lista, 201
        except Exception as e:
            db.session.rollback()
            return {"erro ao adicionar lista": str(e)}, 500

    def createListaAndMontagem(self, dados_nova_lista):
        lista_criada, status_code = self.createLista(dados_nova_lista)
        if status_code != 201:
            return lista_criada, status_code
        dados_nova_montagem = {
            'id_lista': lista_criada.id,
            'id_usuario': None,
            'datetime': datetime_sp_string,
            'status': 0
        }
        try:
            nova_montagem = montagem_schema.load(dados_nova_montagem, session=db.session)
            db.session.add(nova_montagem)
            db.session.commit()
            # Retorne um dicionário serializável, usando dump
            return montagem_schema.dump(nova_montagem), 201, lista_criada
        except Exception as e:
            db.session.rollback()
            return {"erro ao adicionar montagem": str(e)}, 500

    def getAllListas(self):
        try:
            allListas = Lista.query.all()
            return listas_schema.dump(allListas), 200 
        except Exception as e:
            db.session.rollback()
            return {"erro no GET Listas": str(e)}, 404

    def getByIdLista(self, id_lista):
        try:
            byIdLista = Lista.query.get_or_404(id_lista)
            return lista_schema.dump(byIdLista), 200
        except Exception as e:
            return {"erro": str(e)}, 404
        
