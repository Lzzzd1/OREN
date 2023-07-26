from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from src.forms import link_form_builder
from src.models import Cliente

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    return render_template('index.html')


@views.route('/vender')
@login_required
def vender():
    servicos = 'FIP FIM FIS FIE FIV PAM PAE PIEDU'.split()
    print(list(request.form.items()))
    form = link_form_builder(servicos)
    return render_template('cadproposta.html', form=form)


# @views.route('/propostas')
# @login_required
# def propostas():
#     propostas = Venda.query.all()
#     return render_template('acproposta.html', propostas=propostas)


@views.get('/cliente/<cpf>')
def pesquisar(cpf):
    cliente = Cliente.query.filter_by(cpf=cpf).first()
    return render_template('cliente.html', cliente=cliente)


@views.post('/cliente/')
def pesquisar_post():
    dado = request.form.get('cpf').replace('.', '').replace('-', '').replace('(', '').replace(')', '')
    cliente = Cliente.query.filter((Cliente.cpf == dado)).first()
    if not cliente:
        flash('Não encontrado', 'danger')
        return redirect(url_for('.index'))
    return render_template('cliente.html', cliente=cliente)


def configure(app):
    app.register_blueprint(views)
