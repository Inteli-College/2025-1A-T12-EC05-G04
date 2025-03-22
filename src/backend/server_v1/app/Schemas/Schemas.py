from app.Models.MontagemModel import Montagem
from app.Models.ListaModel import Lista
from app.Models.LogsModel import Logs

from app import ma
from marshmallow import INCLUDE
from marshmallow import fields



class MontagemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Montagem
        load_instance = True
        include_fk = True   # Incluir campos de chave estrangeira
        unknown = INCLUDE


class LogsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Logs
        load_instance = True

class ListaSchema(ma.SQLAlchemyAutoSchema):
    montagem = fields.Nested(MontagemSchema, dump_only=True)

    class Meta:
        model = Lista
        load_instance = True
        unknown = INCLUDE  # permite campos não definidos explicitamente

    
