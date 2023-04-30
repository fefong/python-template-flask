import logging
from dotenv import load_dotenv

from flask import Flask
import variables

# load environment variables
load_dotenv()


def create_app():
    app = Flask(__name__)

    # {{ Home }}
    from modules.home.controller import home_controller
    app.register_blueprint(home_controller.blueprint_app)

    # {{ Application }}
    from modules.application.controller import application_controller
    app.register_blueprint(application_controller.blueprint_app)

    # Instance App
    return app


if __name__ == '__main__':
    app = create_app()

    # Settings
    host = variables.HOST
    port = variables.PORT
    debug = variables.DEBUG

    logging.info(f'ApplicationName: {variables.APPLICATION_NAME}')

    app.run(host, port, debug)

