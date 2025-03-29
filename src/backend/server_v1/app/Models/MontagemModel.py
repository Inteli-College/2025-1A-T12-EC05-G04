from app import db

class Montagem(db.Model):
    __tablename__ = 'montagem'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_lista = db.Column(db.Integer, db.ForeignKey('lista.id'), nullable=False, unique=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)

    datetime = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    
    # Relacionamentos
    lista = db.relationship('Lista', back_populates='montagem')
    erros = db.relationship('ErroMontagem', backref='montagem', lazy=True)
    logs = db.relationship('Logs', backref='montagem', lazy=True)
    
    def __repr__(self):
        return f'<Montagem {self.id}>'