from app.Models.MontagemModel import Montagem
from app.Models.ListaModel import Lista
from app.Models.LogsModel import Logs
from app.Models.ErroMontagemModel import ErroMontagem
from app.Models.UsuarioModel import Usuario

from app import ma
from marshmallow import fields


# Validação de dados que entram e saem da aplicação. Promove um design modular. Possibilita a transformação dos dados de objetos em JSON e vice versa.

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

class ErroMontagemSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ErroMontagem
        load_instance = True
        include_fk = True   # inclui os campos de chave estrangeira 

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        include_fk = True   # inclui os campos de chave estrangeira 