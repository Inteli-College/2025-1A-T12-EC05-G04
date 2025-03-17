# Arquivo resposável por modelar/manipular o banco de dados

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


class Lote(db.Model):
    __tablename__ = 'lote'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    remedio = db.Column(db.String(100), nullable=False)
    compostaAtivo = db.Column(db.String(10), nullable=False)
    dose = db.Column(db.String(10), nullable=False)
    validade = db.Column(db.String(10), nullable=False)
    quantidade = db.Column(db.String(10), nullable=False)
    
    # Relacionamentos
    listas = db.relationship('Lista', backref='remedio', lazy=True)
    devolucoes = db.relationship('Devolucao', backref='remedio', lazy=True)
    
    def __repr__(self):
        return f'<Lote {self.remedio}>'


class Lista(db.Model):
    __tablename__ = 'lista'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Removido: id_montagem = db.Column(db.Integer, db.ForeignKey('montagem.id'), nullable=False)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    id_remedio = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    quantidade = db.Column(db.String(10), nullable=False)
    
    # Relacionamento com montagem (inverso)
    montagens = db.relationship('Montagem', backref='lista_principal', lazy=True)
    
    def __repr__(self):
        return f'<Lista {self.id}>'


class Montagem(db.Model):
    __tablename__ = 'montagem'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_lista = db.Column(db.Integer, db.ForeignKey('lista.id'), nullable=False)
    data = db.Column(db.String(10), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    status = db.Column(db.String(1), nullable=False)
    
    # Relacionamentos
    erros = db.relationship('ErroMontagem', backref='montagem', lazy=True)
    
    def __repr__(self):
        return f'<Montagem {self.id}>'


class Devolucao(db.Model):
    __tablename__ = 'devolucao'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.String(20), nullable=False)
    id_remedio = db.Column(db.Integer, db.ForeignKey('lote.id'), nullable=False)
    quantidade = db.Column(db.String(10), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    def __repr__(self):
        return f'<Devolucao {self.id}>'


class ErroMontagem(db.Model):
    __tablename__ = 'erroMontagem'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_montagem = db.Column(db.Integer, db.ForeignKey('montagem.id'), nullable=False)
    mensagem = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'<ErroMontagem {self.id}>'