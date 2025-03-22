from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    CPF = db.Column(db.String(11), nullable=False)
    
    # Relacionamentos
    montagens = db.relationship('Montagem', backref='usuario', lazy=True)
    devolucoes = db.relationship('Devolucao', backref='usuario', lazy=True)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'
