from flask import Flask
from app.views import blueprint_setup

def create_app():
    app = Flask(__name__)
    blueprint_setup(app)
    return app



