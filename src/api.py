from flask import Blueprint, make_response, request, current_app, render_template, url_for
from flask_login import login_required
from src.forms import link_form_builder
from src.models import Links, Cliente, Propostas

api = Blueprint('api', __name__)


@api.post('/links/')
def gerar_link():
    form = link_form_builder('FIP FIM FIS FIE FIV PAM PAE PIEDU'.split())
    if not form.validate():
        resposta = make_response(render_template('htmx/link_form.html', form=form))
        resposta.headers['HX-Retarget'] = '#formProposta'
        return resposta
    cpf = form.cpf.data
    props = request.form.getlist('check')

    if cli := Cliente.query.filter_by(cpf=cpf).first():
        resposta = make_response()
        resposta.headers['HX-Redirect'] = url_for('views.pesquisar', cpf=cli.cpf)
        return resposta
    cliente = Cliente(cpf=cpf)
    current_app.db.session.add(cliente)
    current_app.db.session.commit()
    url = str(current_app.hashid.encode(cliente.id))
    link = Links(link=url)
    cliente.links.append(link)
    for i in props:
        cliente.links[0].propostas.append(Propostas(**{'nome': i}))
    current_app.db.session.commit()
    resposta = make_response(render_template('htmx/link_form.html', form=form, link=request.host_url + url))
    resposta.headers['HX-Retarget'] = '#formProposta'
    return resposta

def configure(app):
    app.register_blueprint(api, url_prefix='/api')
