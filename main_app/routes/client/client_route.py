from flask import Blueprint
import json

client_mod = Blueprint('client', __name__)


@client_mod.route('/')
def client():
    return "<h1>Inside client</h1>"


@client_mod.route('/getIncoterms')
def get_client_incoterm():
    obj = [{'incoterm_id': '1', 'incoterm_name': 'Incoterm A'}, {'incoterm_id': '2', 'incoterm_name': 'Incoterm B'},
           {'incoterm_id': '3', 'incoterm_name': 'Incoterm C'}, {'incoterm_id': '4', 'incoterm_name': 'Incoterm D'}]
    return json.dumps(obj)


@client_mod.route('/getProductCategories')
def get_client_product_categoris():
    obj = [{'category_id': '1', 'category_name': 'Category A'}, {'category_id': '2', 'category_name': 'Category B'},
           {'category_id': '3', 'category_name': 'Category C'}, {'category_id': '4', 'category_name': 'Category D'}]
    return json.dumps(obj)


@client_mod.route('/getLocations')
def get_client_locations():
    obj = [{'location_id': '1', 'location_name': 'location A'}, {'location_id': '2', 'location_name': 'location B'},
           {'location_id': '3', 'location_name': 'location C'}, {'location_id': '4', 'location_name': 'location D'}]
    return json.dumps(obj)
