from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    from . import models, routes, services
    app = Flask(__name__)
    models.init_app(app, db)
    routes.init_app(app)
    # services.init_app(app)
    return app
