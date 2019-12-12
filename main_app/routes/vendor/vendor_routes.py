from flask import Blueprint, send_file

vendor_mod = Blueprint('vendor', __name__)


@vendor_mod.route('/', methods=['GET'])
def vendor():
    return "HELLO VENDOR"


@vendor_mod.route('/exportRFT', methods=['GET'])
def return_files_tut():
    try:
        print("FILE -->")
        local_file_path = 'static/dummy_execl.xlsx'
        return send_file(local_file_path, as_attachment=True)
    except Exception as e:
        return str(e)