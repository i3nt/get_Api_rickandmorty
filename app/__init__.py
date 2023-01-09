from flask import Flask
from app.config import Config
from flask_bootstrap import Bootstrap
from app.routes.morty import morty_ruta
def create_app(): #funcion de fabrica que va a contener todas las instancias de flask
    app = Flask(__name__)
    app.config.from_object(Config)
    Bootstrap(app)
    app.register_blueprint(morty_ruta)
    return app