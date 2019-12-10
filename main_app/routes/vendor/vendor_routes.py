from flask import Blueprint

vendor_mod = Blueprint('vendor', __name__)


@vendor_mod.route('/')
def vendor():
    return "<h1>Inside Vendor</h1>"
