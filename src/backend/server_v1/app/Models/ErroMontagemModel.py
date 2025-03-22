from app import db

class ErroMontagem(db.Model):
    __tablename__ = 'erroMontagem'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_montagem = db.Column(db.Integer, db.ForeignKey('montagem.id'), nullable=False)
    
    mensagem = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<ErroMontagem {self.id}>'