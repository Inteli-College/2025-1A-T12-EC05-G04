from app import db

class Paciente(db.Model):
    __tablename__ = 'paciente'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    HC = db.Column(db.String(20), nullable=False)
    Leito = db.Column(db.String(25), nullable=False)
    
    # Relacionamentos
    listas = db.relationship('Lista', backref='paciente', lazy=True)
    
    def __repr__(self):
        return f'<Paciente {self.nome}>'