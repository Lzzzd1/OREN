from flask import Blueprint, current_app
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from .models import Users, db
from werkzeug.security import generate_password_hash
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.hierarquia >= 4


admin = Admin(name='Administrador', template_mode='bootstrap3', index_view=MyAdminIndexView())

# adm = Blueprint('adm', __name__)

# with current_app.app_context():


class UsersView(ModelView):
    can_export = True

    def _on_model_change(self, form, model, is_created):
        model.senha = generate_password_hash(model.senha, method='sha512')

    def is_accessible(self):
        return current_user.is_authenticated and current_user.hierarquia >= 4

admin.add_view(UsersView(Users, db.session))


def configure(app):
    admin.init_app(app)
