from flask import Blueprint, render_template, redirect, url_for, request, flash
from app.models.character import Character
from app.db import db
import requests

character = Blueprint('character',__name__)

@character.route('/')
def index():
    characters = db.characters.find()
    noneCh = db.characters.find_one({"idRM": 1})
    return render_template('index.html', characters = characters, noneCh = noneCh)

@character.route('/insert')
def insertCharacter():
    for page in range (1,22):
        url = "https://rickandmortyapi.com/api/character?page=" + str(page)
        infoCharacter = requests.get(url).json()["results"]
        for info in infoCharacter:
            _id = info["id"]
            name = info["name"]
            status = info["status"]
            species = info["species"]
            location = info["location"]["name"]
            character = Character(_id, name, status, species, location)

            db.characters.insert_one(character.to_json())
    
    return redirect(url_for('character.index'))

@character.route('/perfil/<idRM>')
def perfil(idRM):
    character = db.characters.find_one({"idRM":int(idRM)})
    return render_template('profile.html', character = character)


