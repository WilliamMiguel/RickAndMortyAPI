from flask import Blueprint, render_template, redirect, url_for
from app.models.character import Character
from app.models.episode import Episode
from app.models.location import Location
from app.db import db
import requests

character = Blueprint('character', __name__)

@character.route('/')
def home():
    noneDB = True
    if not db.characters.find_one() or not db.episodes.find_one():
        noneDB = False

    return render_template('home.html', noneDB=noneDB)

@character.route('/insert-db')
def insertDB():
    #Insert - Personajes
    all_pages = int(requests.get("https://rickandmortyapi.com/api/character").json()["info"]["pages"]) + 1
    for page in range(1, all_pages):
        url = "https://rickandmortyapi.com/api/character?page=" + str(page)
        infoCharacter = requests.get(url).json()["results"]
        for info in infoCharacter:
            _id = info["id"]
            name = info["name"]
            status = info["status"]
            species = info["species"]
            _type = info["type"]
            gender = info["gender"]
            origin = info["origin"]["name"]
            location = info["location"]["name"]
            list_episodes = []
            for episode in info["episode"]:
                dict_episodes = {}
                dict_episodes["id_episode"] = episode.split("/")[-1]
                dict_episodes["name_episode"] = ""
                list_episodes.append(dict_episodes)

            character = Character(_id, name, status, species, _type, gender, origin, location, list_episodes)
            db.characters.insert_one(character.to_json())

    #Insert - Capítulos
    all_episodes = int(requests.get("https://rickandmortyapi.com/api/episode").json()["info"]["pages"]) + 1
    for page in range(1, all_episodes):
        url = "https://rickandmortyapi.com/api/episode?page=" + str(page)
        infoEpisode = requests.get(url).json()["results"]
        for info in infoEpisode:
            _id = info["id"]
            name = info["name"]
            link_characters = info["characters"]
            list_characters = []
            for character in link_characters:
                dict_characters = {}
                dict_characters["id_character"] = character.split("/")[-1]
                dict_characters["name_character"] = ""
                list_characters.append(dict_characters)

            episode = Episode(_id, name, list_characters)
            db.episodes.insert_one(episode.to_json())

    #Insert - Locations
    all_locations = int(requests.get("https://rickandmortyapi.com/api/location").json()["info"]["pages"]) + 1
    for page in range(1, all_locations):
        url = "https://rickandmortyapi.com/api/location?page=" + str(page)
        infoLocation = requests.get(url).json()["results"]
        for info in infoLocation:
            _id = info["id"]
            name = info["name"]
            dimension = info["dimension"]
            link_characters = info["residents"]
            list_characters = []
            for character in link_characters:
                dict_characters = {}
                dict_characters["id_character"] = character.split("/")[-1]
                dict_characters["name_character"] = ""
                list_characters.append(dict_characters)

            location = Location(_id, name, dimension, list_characters)
            db.locations.insert_one(location.to_json())

    #Actualización de campos        

    # Rellenar el campo "list_episodes["name_episodes"]". Colección: Characters
    characters = db.characters.find()
    noneCh = db.characters.find_one()
    if noneCh is None:
        return redirect(url_for('character.home'))
    else:
        for character in characters:
            idch = character["idRM"]
            episodes = character["list_episodes"]
            location = character["location"]
            count = 0
            for episode in episodes:
                name_episode = db.episodes.find_one({"idE": int(episode["id_episode"])}, {"name": 1})["name"]
                db.characters.update_one({"idRM": idch}, {"$set": {"list_episodes." + str(count) + ".name_episode": name_episode}})
                count += 1

            if location == "unknown":
                name_dimension = "Unknown"
            else:
                name_dimension = db.locations.find_one({"name": location}, {"dimension": 1})["dimension"]
            
            db.characters.update_one({"idRM": idch}, {"$set": {"dimension": name_dimension}})

    # Rellenar el campo "list_characters["name_character"]" en cada capítulo. Colección: Episodes
    episodes = db.episodes.find()
    noneEp = db.episodes.find_one()
    if noneEp is None:
        return redirect(url_for('character.home'))
    else:
        for episode in episodes:
            nameEpisode = episode["name"]
            characters = episode["list_characters"]
            count = 0
            for character in characters:
                name_character = db.characters.find_one({"idRM": int(character["id_character"])}, {"name": 1})["name"]
                db.episodes.update_one({"name": nameEpisode}, {"$set": {"list_characters." + str(count) + ".name_character": name_character}})
                count += 1
    
    # Rellenar el campo "list_characters["name_character"]" en cada location. Colección: Locations
    locations = db.locations.find()
    noneLc = db.locations.find_one()
    if noneLc is None:
        return redirect(url_for('character.home'))
    else:
        for location in locations:
            nameLocation = location["name"]
            characters = location["list_characters"]
            count = 0
            for character in characters:
                name_character = db.characters.find_one({"idRM": int(character["id_character"])}, {"name": 1})["name"]
                db.locations.update_one({"name": nameLocation}, {"$set": {"list_characters." + str(count) + ".name_character": name_character}})
                count += 1
            
    return redirect(url_for('character.home'))

@character.route('/characters')
def listcharacters():
    characters = db.characters.find().sort("idRM", -1)
    noneCh = db.characters.find_one()
    return render_template('list_characters.html', characters=characters, noneCh=noneCh)

@character.route('/characters/<idRM>')
def profile(idRM):
    character = db.characters.find_one({"idRM": int(idRM)})
    episodes = db.episodes.find({}, {"idE": 1, "name": 1})
    if character is None:
        return render_template('E404.html')

    return render_template('character.html', character=character, episodes=episodes)

@character.route('/capitulos')
def listepisodes():
    episodes = db.episodes.find().sort("idE")
    noneEp = db.episodes.find_one()
    return render_template('list_episodes.html', episodes=episodes, noneEp=noneEp)

@character.route('/capitulos/<id>')
def episode(id):
    episode = db.episodes.find_one({"idE": int(id)})
    characters = db.characters.find()
    if episode is None:
        return render_template('E404.html')

    return render_template('episode.html', episode=episode, characters = characters)

def status_404(e):
    return render_template('E404.html'), 404