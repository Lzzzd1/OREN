from flask import Blueprint, jsonify
from flask_login import login_required
from src.models import Produto

api = Blueprint('api', __name__)


@api.get('/preco/<int:id>')
@login_required
def preco(id):
    produto = Produto.query.filter_by(id=id).first()
    return jsonify(preco=produto.valor if produto else False)


def configure(app):
    app.register_blueprint(api, url_prefix='/api')
