from flask import Blueprint, render_template

err_mod = Blueprint('error_handler', __name__)


@err_mod.app_errorhandler(404)
def page_not_found(e):
    """ Return error 404 """
    return render_template('not_found.html')
