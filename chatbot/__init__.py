from flask import Flask
from .routes.base import base

def create_app():
    app = Flask(__name__)

    route_files = ["base"]
    app.register_blueprint(base, url_prefix = '/')

    return app