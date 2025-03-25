from app.Models.MontagemModel import Montagem
from app.Models.ListaModel import Lista
from app.Models.LogsModel import Logs
from app.Models.ErroMontagemModel import ErroMontagem
from app.Models.InstrucaoRoboModel import InstrucaoRobo

from app import ma
from marshmallow import fields



class MontagemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Montagem
        load_instance = True
        include_fk = True   # Incluir campos de chave estrangeira

class LogsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Logs
        load_instance = True
        include_fk = True   # inclui os campos de chave estrangeira

class ListaSchema(ma.SQLAlchemyAutoSchema):
    montagem = fields.Nested(MontagemSchema, dump_only=True)

    class Meta:
        model = Lista
        load_instance = True
        include_fk = True   # Incluir campos de chave estrangeira

class ErroMontagemScema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ErroMontagem
        load_instance = True
        include_fk = True   # inclui os campos de chave estrangeira 

class InstrucaoRoboSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InstrucaoRobo
        load_instance = True
        include_fk = True   # inclui os campos de chave estrangeira 
