from flask import Blueprint

client_mod = Blueprint('client', __name__)


@client_mod.route('/')
def client():
    return "<h1>Inside client</h1>"


@client_mod.app_errorhandler(404)
def page_not_found(e):
    """ Return error 404 """
    return "SUP ?"
