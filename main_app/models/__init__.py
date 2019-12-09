from config import APP_VAR


def init_app(app, db):
    db_url = f'postgresql+psycopg2://{APP_VAR["POSTGRES_USER"]}:{APP_VAR["POSTGRES_PW"]}@{APP_VAR["POSTGRES_URL"]}/{APP_VAR["POSTGRES_DB"]}'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
    db.init_app(app)

    from .vendor import Vendor

    return db
