from flask import Blueprint, redirect, url_for, request, current_app, flash, jsonify
from flask_login import login_required
from src.models import Links, Cliente

api = Blueprint('api', __name__)


@api.post('/links/')
def gerar_link():
    cpf = request.form.get('cpf')
    cliente = Cliente(cpf=cpf)
    current_app.db.session.add(cliente)
    current_app.db.session.commit()
    url = str(current_app.hashid.encode(cliente.id))
    link = Links(link=url)
    cliente.links.append(link)
    current_app.db.session.commit()
    # flash(url, 'primary')
    # return redirect(url_for('views.vender'))
    return jsonify(url=request.host_url + url)

def configure(app):
    app.register_blueprint(api, url_prefix='/api')
