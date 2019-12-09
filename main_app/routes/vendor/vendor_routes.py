from flask import Blueprint

vendor_mod = Blueprint('vendor', __name__)


@vendor_mod.route('/')
def vendor():
    return "<h1>Inside Vendor</h1>"


@vendor_mod.app_errorhandler(404)
def page_not_found(e):
    """ Return error 404 """
    return "SUP ?"
