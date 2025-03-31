from app.Models.UsuarioModel import Usuario, db
from app.Schemas.Schemas import UsuarioSchema
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import SQLAlchemyError

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

class UsuarioController:

    def __init__(self):
        pass

    def login(self, dados_auth_usuario):
        try:
            email = dados_auth_usuario.get('email')
            senha = dados_auth_usuario.get('senha')

            if not email or not senha:
                return {'erro': 'Email e senha são obrigatórios.'}, 400

            usuario = Usuario.query.filter_by(email=email).first()

            if not usuario:
                return {'erro': 'Email não encontrado'}, 404

            if not check_password_hash(usuario.senha, senha):
                return {'erro': 'Senha incorreta'}, 401

            return {
                'mensagem': 'Login realizado com sucesso',
                'usuario': usuario_schema.dump(usuario)
            }, 200

        except Exception as e:
            return {'erro': f'Erro interno: {str(e)}'}, 500
    
    def createUsuario(self, dados_new_user):
        try:
            dados_new_user["senha"] = generate_password_hash(dados_new_user["senha"])
            new_user = usuario_schema.load(dados_new_user, session=db.session)
            db.session.add(new_user)
            db.session.flush()
            db.session.commit()
            return usuario_schema.dump(new_user), 201
        except SQLAlchemyError as e:
            print("[ERRO SQL]", e)
            db.session.rollback()
            return {"erro": str(e)}, 500