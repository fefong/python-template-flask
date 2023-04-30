from flask import Blueprint, render_template

import variables
from modules.common.utilities import get_path_dirname

template_path = get_path_dirname('modules/home/templates/')
blueprint_app = Blueprint("home", __name__, template_folder=template_path)


@blueprint_app.route("/", methods=["GET"])
def get_index():
    application_name = variables.APPLICATION_NAME
    return render_template('index.html', **locals())
