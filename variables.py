import logging

import os


def get_env(key: str, default: any):
    return os.environ[key] if key in os.environ != '' else default


# Settings
HOST = get_env(key="HOST", default="0.0.0.0")
PORT = get_env(key="PORT", default="5000")
DEBUG = get_env(key="DEBUG", default='False').capitalize() == 'True'
logging.root.setLevel(get_env(key="LOG_LEVEL", default="INFO"))

# Application
APPLICATION_NAME = get_env(key="APPLICATION_NAME", default="MY APPLICATION")
