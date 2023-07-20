from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin


db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    nome = db.Column(db.String(25), nullable=False)
    senha = db.Column(db.String, nullable=False)
    hierarquia = db.Column(db.Integer, nullable=False)

    vendas = db.relationship('Venda', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'User {self.nome}'


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(60))
    nasc = db.Column(db.Date)
    email = db.Column(db.String(50))
    cpf = db.Column(db.String(20), index=True, unique=True)
    rg = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return f'Cliente: {self.nome[:10]}'


class Endereco(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    cep = db.Column(db.String(8))
    uf = db.Column(db.String(2))
    cidade = db.Column(db.String)
    bairro = db.Column(db.String)
    rua = db.Column(db.String)
    numero = db.Column(db.Integer)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    cliente = db.relationship('Cliente', backref='enderecos')


class Telefone(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    telefone = db.Column(db.String(13), index=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    cliente = db.relationship('Cliente', backref='telefones')
    vendas = db.relationship('Venda', backref='telefone')

    def __repr__(self):
        return f'Telefone: {self.telefone}'


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(50))
    valor = db.Column(db.Numeric(8, 2))
    custo = db.Column(db.Numeric(8, 2))
    ativo = db.Column(db.Boolean, default=False)

    def __str__(self):
        return str(self.nome)


class Origem(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(30))
    ativo = db.Column(db.Boolean, default=False)

    def __str__(self):
        return str(self.nome)


class Campanha(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(30))
    ativo = db.Column(db.Boolean, default=False)

    def __str__(self):
        return str(self.nome)


class CanalDaVenda(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(30))
    ativo = db.Column(db.Boolean, default=False)


class FormaPagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(30))
    ativo = db.Column(db.Boolean, default=False)


class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    data_pagamento = db.Column(db.DateTime(timezone=False), default=db.func.now(), index=True)
    data_validade = db.Column(db.Date, index=True)
    valor = db.Column(db.Numeric(8, 2))

    venda_id = db.Column(db.Integer, db.ForeignKey('venda.id'), nullable=False)
    formapagamento_id = db.Column(db.Integer, db.ForeignKey(FormaPagamento.id), nullable=False)


class Venda(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    desconto = db.Column(db.Numeric(8, 2))
    total = db.Column(db.Numeric(8, 2))
    data = db.Column(db.DateTime(timezone=False), default=db.func.now())

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    telefone_id = db.Column(db.Integer, db.ForeignKey('telefone.id'), nullable=False)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    origem_id = db.Column(db.Integer, db.ForeignKey('origem.id'), nullable=False)
    campanha_id = db.Column(db.Integer, db.ForeignKey('campanha.id'), nullable=False)
    canaldavenda_id = db.Column(db.Integer, db.ForeignKey(CanalDaVenda.id), nullable=False)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    cliente = db.relationship('Cliente', backref='vendas')
    produto = db.relationship('Produto', backref='vendas')
    origem = db.relationship('Origem', backref='vendas')
    campanha = db.relationship('Campanha', backref='vendas')
    canal = db.relationship('CanalDaVenda', backref='vendas')
    pagamentos = db.relationship('Pagamento', backref='venda', lazy='dynamic')


def configure(app):
    db.init_app(app)
    Migrate(app, db)
    app.db = db
