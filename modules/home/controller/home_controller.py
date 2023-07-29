import random

from flask import Blueprint, render_template, jsonify

import variables
from modules.common.utilities import get_path_dirname

template_path = get_path_dirname('modules/home/templates/')
blueprint_app = Blueprint("home", __name__, template_folder=template_path)


@blueprint_app.route("/", methods=["GET"])
def get_index():
    application_name = variables.APPLICATION_NAME
    time_update_boxes = 5000
    return render_template('index.html', **locals())


@blueprint_app.route('/update_box1')
def update_box1():
    random_number = random.randint(1, 100)
    return jsonify(content=random_number)


@blueprint_app.route('/update_box2')
def update_box2():
    random_number = random.randint(1, 100)
    return jsonify(content=random_number)


@blueprint_app.route('/update_box3')
def update_box3():
    random_number = random.randint(1, 100)
    return jsonify(content=random_number)
