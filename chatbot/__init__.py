from flask import Flask
from .routes.base import base
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)
    route_files = ["base"]
    app.register_blueprint(base, url_prefix = '/')

    return app