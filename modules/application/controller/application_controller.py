from json import JSONDecodeError

from flask import Blueprint, render_template, json, request

import variables
from modules.application.model.application import Application
from modules.application.service import application_service as service
from modules.common import utilities, responses
from modules.common.utilities import get_path_dirname

template_path = get_path_dirname('modules/application/templates')
blueprint_app = Blueprint("application", __name__,
                          url_prefix="/application",
                          template_folder=template_path)


@blueprint_app.route("/", methods=["GET"])
def get_list_application():
    application_name = variables.APPLICATION_NAME
    applications = service.get_applications()
    return render_template('application_page.html', **locals())


@blueprint_app.route("/<id>/", methods=["GET"])
def get_application(id=None):
    try:
        application = service.get_application(id)
        return application

    except Exception:
        return responses.not_found("Application not found")


@blueprint_app.route("/", methods=["POST"])
def post_application():
    mandatory_keys = ['id', 'name', 'email']
    message_missing = f"Required information is missing or not valid: {mandatory_keys}"

    try:
        data = json.loads(request.data, strict=False)
        if not utilities.check_list_exists_in_dict(mandatory_keys, data):
            return responses.bad_request(message_missing)
    except JSONDecodeError:
        return responses.bad_request(message_missing)

    application_id = service.create_application( data['id'], data['name'])

    return responses.ok(f"Application '{application_id}' created")


@blueprint_app.route("/<id>/", methods=["PUT"])
def put_application(id=None):
    mandatory_keys = ['name', 'email']
    message_missing = f"Required information is missing or not valid: {mandatory_keys}"

    try:
        data = json.loads(request.data, strict=False)
        if not utilities.check_list_exists_in_dict(mandatory_keys, data):
            return responses.bad_request(message_missing)
    except JSONDecodeError:
        return responses.bad_request(message_missing)

    application = Application(name=data['name'], email=data['email'])
    application_id = service.update_full_application(id, application)

    return responses.ok(f"Application '{application_id}' udpated")


@blueprint_app.route("/<id>/", methods=["PATCH"])
def patch_application(id=None):
    mandatory_keys = ['name', 'email']
    message_missing = f"Required information is missing or not valid: {mandatory_keys}"

    data = json.loads(request.data, strict=False)
    application_name, application_email = None, None
    if 'name' in data:
        application_name = data['name']
    if 'email' in data:
        application_email = data['email']

    if application_name is None and application_email is None:
        return responses.bad_request(message_missing)

    application = Application(name=application_name, email=application_email)
    application_id = service.update_application(id, application)

    return responses.ok(f"Application '{application_id}' udpated")


@blueprint_app.route("/<id>/", methods=["DELETE"])
def delete_application(id=None):
    try:
        application_id = service.delete_application(id)
        return responses.ok(f"Application '{application_id}' deleted")
    except Exception:
        return responses.bad_request(f"Application '{id}' not found")
