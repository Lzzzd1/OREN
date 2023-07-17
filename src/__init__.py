from flask import Flask
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from src.auth import configure as auth_config
from src.views import configure as views_config
from src.models import configure as db_config
from src.adm import configure as adm_config
from src.models import Users


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '230894ruw2ru9wuef9aue90fu90fuwdufisdou9sdufwpwe9fw04r9sdposdçflj'
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///teste.db'
    db_config(app)
    app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
  #  app.debug = True
   # toolbar = DebugToolbarExtension()
    #toolbar.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Você precisa estar logado!'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_):
        return Users.query.get(int(id_))

    adm_config(app)

    auth_config(app)
    views_config(app)

    return app
