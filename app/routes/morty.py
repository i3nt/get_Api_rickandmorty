#blueprint,manejo de rutas pero con nombre especifico
from flask import Blueprint,render_template
import requests
morty_ruta=Blueprint('morty_ruta',__name__)
@morty_ruta.route('/')
def index():
    # return 'hola'
    url = "https://rickandmortyapi.com/api/character"
    informacion =requests.get(url).json()["results"]
    return informacion