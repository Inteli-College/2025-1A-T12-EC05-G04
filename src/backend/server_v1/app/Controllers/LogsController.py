from app.Models.LogsModel import Logs, db
from app.Schemas.Schemas import LogsSchema
from flask import jsonify, request
from app.datetime import datetime_sp_string

logs_schema = LogsSchema()
logs_schema = LogsSchema(many=True)

class LogsController:

    def __init__(self):
        pass

    # def createLog (Recebe um pin, id_montagem, id_remedio)

    def createLog(self, dados_novo_log):
        try:
            novo_log = Logs.load(dados_novo_log, session=db.session)
            db.session.add(novo_log)
            db.session.commit()
            return logs_schema.dump(novo_log), 201
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 500

    def getAllLogs(self):
        try:        
            allLogs = Logs.query.all()
            return logs_schema.dump(allLogs), 200
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 404

    def getByIdLog(self, log_id):
        try:
            ByIdLog = Logs.query.get_or_404(log_id)
            return logs_schema.dump(ByIdLog), 200
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 404

