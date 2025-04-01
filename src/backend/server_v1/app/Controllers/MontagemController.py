from app.Models.MontagemModel import Montagem, db
from app.Models.ErroMontagemModel import ErroMontagem
from app.Schemas.Schemas import MontagemSchema, ErroMontagemSchema

montagem_schema = MontagemSchema()
montagens_schema = MontagemSchema(many=True)

erroMontagem_schema = ErroMontagemSchema()
erroMontagens_schema = ErroMontagemSchema(many=True)


class MontagemController:

    def __init__(self):
        pass

    # A criação (POST) de Montagens é feita pelo ListaController

    def getAllMontagem(self):
        try:
            allMontagem = Montagem.query.all()
            return montagens_schema.dump(allMontagem), 200
        except Exception as e:
            return {"erro": str(e)}, 404

    def getByIdMontagem(self, id_montagem):
        try:
            ByIdmontagem = Montagem.query.get_or_404(id_montagem)
            return montagem_schema.dump(ByIdmontagem), 200
        except Exception as e:
            return {"erro": str(e)}, 404
        
    def getPendentesMontagem(self):
        try:
            pendentesMontagem = Montagem.query.filter(Montagem.status == '0').all()
            return montagens_schema.dump(pendentesMontagem), 200
        except Exception as e:
            return {"erro": str(e)}, 404
        
    def deleteMontagem(self, id_montagem):
        montagem = Montagem.query.get_or_404(id_montagem)
        try:
            db.session.delete(montagem)
            db.session.commit()
            return montagem_schema.dump(montagem), 200
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 404

    def updateMontagem(self, id_montagem, dados_update_montagem):
        try:
            # Filtra pela montagem com o id informado e atualiza com os dados fornecidos
            update_montagem = Montagem.query.filter(Montagem.id == id_montagem).update(dados_update_montagem)
            if update_montagem == 0:
                return {"erro": "Montagem não encontrada"}, 404
            db.session.commit()
            updated_montagem = Montagem.query.get(id_montagem)
            return montagem_schema.dump(updated_montagem), 200
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 404

    def createErroMontagem(self, dados_novo_erroMontagem):
        try:
            novo_erroMontagem = erroMontagem_schema.load(dados_novo_erroMontagem, session=db.session)
            db.session.add(novo_erroMontagem)
            db.session.commit()
            return erroMontagem_schema.dump(novo_erroMontagem), 201
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 500
    
    def getAllErroMontagem(self):
        try:
            allErroMontagem = ErroMontagem.query.all()
            return erroMontagens_schema.dump(allErroMontagem), 200
        except Exception as e:
            return {"erro": str(e)}, 404
