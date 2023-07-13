from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin


db = SQLAlchemy()


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    nome = db.Column(db.String(25), nullable=False)
    senha = db.Column(db.String, nullable=False)
    hierarquia = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'


def configure(app):
    db.init_app(app)
    Migrate(app, db)
    app.db = db
