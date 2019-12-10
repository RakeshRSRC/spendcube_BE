from flask import Blueprint

vendor_mod = Blueprint('vendor', __name__)


@vendor_mod.route('/', methods=['GET'])
def vendor():
    print("YASSS")
    return "HELLO VENDOR"
