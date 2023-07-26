from flask import Blueprint, current_app, g, abort
from src.models import Links


lead = Blueprint('lead', __name__)


@lead.url_value_preprocessor
def get_cliente(endpoint, values):
    hashh = values.pop('hashdd')
    id = current_app.hashid.decode(hashh)
    # if not id:
    #     return abort(404)
    link = Links.query.get_or_404(id[0])
    g.cliente = link.cliente


@lead.get('/')
def oi():
    return f'{g.cliente.cpf}'


def configure(app):
    app.register_blueprint(lead, url_prefix='/<hashdd>')
