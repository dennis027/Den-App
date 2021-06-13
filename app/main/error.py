from flask import render_template
from . import main
@main.app_errorhandler(404)
def four_Ow_four(error):
    """
    function to render error apge
    """
    return render_template('fourOwFour.html'),404