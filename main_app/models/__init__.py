# from flask_sqlalchemy import SQLAlchemy
from config import POSTGRES_DB, POSTGRES_PW, POSTGRES_URL, POSTGRES_USER


def init_app(app, db):
    db_url = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
    db.init_app(app)

    from .vendor import Vendor

    return db
