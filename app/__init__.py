from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import Config
from .routes.characters import character

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(character)
    Bootstrap(app)
    return app