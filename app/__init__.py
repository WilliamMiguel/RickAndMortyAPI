from flask import Flask
from app.config import Config
from .routes.characters import character

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(character)

    from app.routes.characters import status_404
    app.register_error_handler(404, status_404)

    return app