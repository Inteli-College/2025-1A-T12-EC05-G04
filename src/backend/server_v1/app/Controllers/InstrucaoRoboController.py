from app.Models.InstrucaoRoboModel import InstrucaoRobo, db
from app.Schemas.Schemas import InstrucaoRoboSchema

InstrucaoRobo_schema = InstrucaoRoboSchema()

class InstrucaoRoboController:

    def __init__(self):
        pass

    def getByIdInstrucaoRobo(self, instrucaoRobo_id):
        try:
            ByIdInstrucaoRobo = InstrucaoRobo.query.get_or_404(instrucaoRobo_id)
            return InstrucaoRobo_schema.dump(ByIdInstrucaoRobo), 200
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 404
