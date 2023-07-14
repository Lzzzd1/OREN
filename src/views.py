from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def index():
    return render_template('index.html')


@views.route('/vender')
@login_required
def vender():
    return render_template('cadproposta.html')


@views.route('/propostas')
@login_required
def propostas():
    return render_template('acproposta.html')


def configure(app):
    app.register_blueprint(views)
