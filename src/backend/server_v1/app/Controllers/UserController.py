from app.Models.UsuarioModel import Usuario, db
from app.Schemas.Schemas import UsuarioSchema
from werkzeug.security import check_password_hash, generate_password_hash

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

class UsuarioController:

    def __init__(self):
        pass

    def login (self, dados_auth_user):
        try:
            email = dados_auth_user.email.get('email')
            senha = dados_auth_user.senha.get('senha') 

            usuario = Usuario.query.filter_by(email=email).first()

            if not usuario:
                
                return {'erro' : 'Email não encontrado'}, 404
        
            if not check_password_hash(usuario.senha, senha):
                return {'erro' : 'Senha incorreta'}, 401
    
            return {
            'mensagem': 'Login realizado com sucesso',
            'usuario': usuario_schema.dump(usuario)
            }, 200

        except Exception as e:
            return {"erro": str(e)}, 404
    
    def createUser (self, dados_new_user):
        try:
            dados_new_user.senha = generate_password_hash(dados_new_user.senha)

            new_user = usuario_schema.load(dados_new_user, session=db.session)
            db.session.add(new_user)
            db.session.commit()
            return usuario_schema.dump(new_user), 201
        except Exception as e:
            db.session.rollback()
            return {"erro": str(e)}, 500