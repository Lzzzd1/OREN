from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, StringField
from wtforms.validators import DataRequired, InputRequired, Length, EqualTo


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