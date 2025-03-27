from app import db

class Lote(db.Model):
    __tablename__ = 'lote'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    remedio = db.Column(db.String(100), nullable=False)
    compostoAtivo = db.Column(db.String(10), nullable=False)  
    dose = db.Column(db.String(10), nullable=False)
    validade = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    codigo = db.Column(db.String(100), nullable=False)
    
    # Relacionamentos
    listas = db.relationship('Lista', backref='lote', lazy=True)
    devolucoes = db.relationship('Devolucao', backref='lote', lazy=True)
    logs = db.relationship('Logs', backref='lote', lazy=True)

    # Relacionamento 1:1 com Montagem
    instrucaoRobo = db.relationship('InstrucaoRobo', uselist=False, back_populates='lote')

    def __repr__(self):
        return f'<Lote {self.remedio}>'