from flask import Blueprint, current_app
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from src.models import Users, Telefone, Cliente, Origem, Propostas, Campanha, Links, db
from werkzeug.security import generate_password_hash
from flask_login import current_user


class MyAdminIndexView(AdminIndexView):
    # def is_accessible(self):
    #     return current_user.is_authenticated and current_user.hierarquia >= 4
    ...


admin = Admin(name='Administrador', template_mode='bootstrap3', index_view=MyAdminIndexView())


class MyView(ModelView):
    # column_display_all_relations = True
    # column_hide_backrefs = False
    ...


class TelefoneView(ModelView):
    column_list = ['telefone', 'cliente']


class UsersView(MyView):
    can_export = True

    def _on_model_change(self, form, model, is_created):
        model.senha = generate_password_hash(model.senha, method='sha512')

    # def is_accessible(self):
    #     return current_user.is_authenticated and current_user.hierarquia >= 4


admin.add_view(UsersView(Users, db.session))
admin.add_view(MyView(Cliente, db.session, 'Cliente'))
admin.add_view(TelefoneView(Telefone, db.session, 'Telefone'))
admin.add_view(MyView(Origem, db.session, 'Origem'))
admin.add_view(MyView(Campanha, db.session, 'Campanha'))
admin.add_view(MyView(Propostas, db.session, 'Propostas'))
admin.add_view(MyView(Links, db.session, 'Links'))


def configure(app):
    admin.init_app(app)
