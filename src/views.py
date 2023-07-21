from flask import Blueprint, render_template, request
from flask_login import login_required
from src.forms import ClienteForm, PropostaForm, VendaMixinForm
from src.models import Cliente, Venda, Produto

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    return render_template('index.html')


@views.route('/vender')
@login_required
def vender():
    form = VendaMixinForm()
    return render_template('cadproposta.html', form=form)


@views.route('/propostas')
@login_required
def propostas():
    propostas = Venda.query.all()
    return render_template('acproposta.html', propostas=propostas)


@views.get('/teste')
def teste():
    form = PropostaForm()
    return render_template('testeform.html', form=form)


def configure(app):
    app.register_blueprint(views)
