from .client.client_route import client_mod
from .vendor.vendor_routes import vendor_mod


def init_app(app):
    app.register_blueprint(client_mod, url_prefix="/client")
    app.register_blueprint(vendor_mod, url_prefix="/vendor")
