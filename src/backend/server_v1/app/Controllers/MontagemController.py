from app.Models.MontagemModel import Montagem, db
from app.Schemas.Schemas import MontagemSchema
from marshmallow import ValidationError

montagem_schema = MontagemSchema()
montagens_schema = MontagemSchema(many=True)

class MontagemController:

    def __init__(self):
        pass

    # A criação (POST) de Montagens é feita pelo ListaController, por conta da lógica de negócio seguida pela nossa aplicação

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
            return {"erro": str(e)}, 500

    # def updateMontagem(self, dados_update_montagem, id_montagem):
    #         try:
    #             montagem_update = Montagem.query.get_or_404(id_montagem)

    #             if dados_update_lista.id == id_montagem:
    #                 db.session.commit()
    #             return montagem_schema.dump(montagem_update), 200
    #         except ValidationError as e:
    #             db.session.rollback()
    #             return {"erro": str(e)}, 400
        
        
