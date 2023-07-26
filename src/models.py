from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    nome = db.Column(db.String(25), nullable=False)
    senha = db.Column(db.String, nullable=False)
    hierarquia = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, email, nome, senha):
        self.email = email
        self.nome = nome
        self.senha = generate_password_hash(senha, method='sha512')

    def __repr__(self):
        return f'User {self.nome}'


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    nome = db.Column(db.String(60))
    nasc = db.Column(db.Date)
    email = db.Column(db.String(50))
    cpf = db.Column(db.String(20), index=True, unique=True)
    rg = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return f'Cliente: {self.cpf}'


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

    def __repr__(self):
        return f'Telefone: {self.telefone}'


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

    def __repr__(self):
        return str(self.nome)


class FormaPagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(30))
    ativo = db.Column(db.Boolean, default=False)


class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    data_pagamento = db.Column(db.DateTime(timezone=False), default=db.func.now(), index=True)
    data_validade = db.Column(db.Date, index=True)
    valor = db.Column(db.Numeric(8, 2))

    formapagamento_id = db.Column(db.Integer, db.ForeignKey(FormaPagamento.id), nullable=False)


class Propostas(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    nome = db.Column(db.String(50))
    ativo = db.Column(db.Boolean, default=False)

    def __str__(self):
        return str(self.nome)


links_e_props = db.Table('links_e_props',
                         db.Column('link_id', db.Integer, db.ForeignKey('links.id')),
                         db.Column('proposta_id', db.Integer, db.ForeignKey('propostas.id'))
                         )


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    criada = db.Column(db.DateTime(timezone=False), default=db.func.now())
    link = db.Column(db.String)
    acessos = db.Column(db.Integer)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    cliente = db.relationship('Cliente', backref=db.backref('links', lazy='dynamic'))
    propostas = db.relationship('Propostas', secondary=links_e_props, backref='links')


def configure(app):
    db.init_app(app)
    Migrate(app, db)
    app.db = db
