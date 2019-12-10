from flask import Blueprint

client_mod = Blueprint('client', __name__)


@client_mod.route('/')
def client():
    return "<h1>Inside client</h1>"