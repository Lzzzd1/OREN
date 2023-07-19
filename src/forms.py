from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, StringField, DateField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo

from src.constants import UFS


class LoginForm(FlaskForm):
    usuario = EmailField('Usuário', validators=[DataRequired(message='Precisamos do seu email!')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Precisamos da sua senha!')])
    lembrar = BooleanField('Lembrar-se')


class RegisForm(FlaskForm):
    nome = StringField('Nome', validators=[InputRequired(),
                                           Length(min=1, max=25, message='Nome muito longo!')])
    email = EmailField('Email', validators=[InputRequired(message='O usuário precisa logar!')])
    senha = PasswordField('Senha', validators=[InputRequired('O usuário precisa de senha!'),
                                               Length(min=8)])
    confirmar_senha = PasswordField('Confirmar senha', validators=[InputRequired('O usuário precisa de senha!'),
                                                                   EqualTo('senha', message='As senhas não batem!')])


class ClienteForm(FlaskForm):
    cpf = StringField('CPF', validators=[InputRequired(), Length(min=11, max=20, message='CPF Inválido')])
    rg = StringField('RG', validators=[InputRequired(), Length(min=7, max=20)])
    nome = StringField('Nome Completo', validators=[InputRequired(), Length(min=1, max=50, message='Nome muito longo!')])
    nasc = DateField('Data de Nascimento', format='%d-%m-%Y', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    telefone = StringField('Telefone', validators=[InputRequired()])


class EnderecoForm(FlaskForm):
    cep = StringField('CEP', validators=[InputRequired(), Length(min=8, max=8)])
    uf = SelectField('UF', choices=[(uf, uf) for uf in UFS], validators=[InputRequired()])
    bairro = StringField('Bairro', validators=[InputRequired()])
    cidade = StringField('Cidade', validators=[InputRequired()])
    rua = StringField('Rua', validators=[InputRequired()])
    numero = IntegerField('Número', validators=[InputRequired()])


class PropostaForm(FlaskForm):
    telefone_venda = SelectField('Telefone do contato', choices=[(f'telefone{x}', f'telefone{x}') for x in range(3)])
    produto = SelectField('Plano', choices=[(f'plano{x}', f'plano{x}') for x in range(3)])
    desconto = FloatField('Desconto')
    total = FloatField('Total')
    origem = SelectField('Origem', choice=[(f'origem{x}', f'origem{x}') for x in range(3)])
    campanha = SelectField('Campanha', choice=[(f'campanha{x}', f'campanha{x}') for x in range(3)])
    canal = SelectField('Canal da venda', choices=[(f'canal{x}', f'canal{x}') for x in range(3)])

