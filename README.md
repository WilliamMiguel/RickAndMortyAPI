# Rick and Morty - MongoDB

Proyecto con Flask y MongoDB usando la API "Rick and Morty" (https://rickandmortyapi.com)

## Instalación
Crear una carpeta e iniciar VS Code dentro de ella, luego crear el entorno virtual ejecutando la siguiente línea:

```bash
py -m venv env
```
Acceder al entorno virtual y activarlo. En Windows:

```bash
.\env\scripts\activate
```

Instalar las dependencias que se encuentran en requirements.txt:

```bash
pip install -r requirements.txt
```

Crear un archivo **.env** afuera de la carpeta app con las siguientes variables:
```py
FLASK_APP = main.py
FLASK_DEBUG = True
FLASK_ENV = development
SECRET_KEY = #Ingresa una clave secreta
```

## Uso

Ejecutar la siguiente línea de código dentro del entorno virtual:
```python
flask run
```
Luego acceder al localhost: http://127.0.0.1:5000/ y hacer click en **Insertar personajes** para crear la base de datos, posteriormente no se mostrará esta opción. De esta forma se cargan todos los personajes, episodios y locaciones.

## Estructura principal del proyecto

### app/routes/characters.py

- Se inicia importanto las librerías o clases necesarias y posteriormente se asigna un nuevo nombre a la app: characters
- Se definen las rutas y funciones:
    - <code>'/'</code>: página principal.
    - <code>'/insert-db</code>: inserta la base de datos, colecciones y documentos. Tiene dos partes, en la primera crea las colecciones: <code>characters</code>,                  <code>episodes</code> y <code>locations</code>, y en la segunda actualiza algunos valores de sus campos.
    - <code>'/characters'</code>: muestra la lista de personajes.
    - <code>'/characters/<idRM>'</code>: muestra el perfil de un personaje.
    - <code>'/episodes'</code>: muestra la lista de capítulos.
    - <code>'/episodes/<id>'</code>: muestra los personajes en un capítulo.

### app/models

Se crean 3 archivos para distinguir cada colección:
  - <code>characters.py</code>
  - <code>episodes.py</code>
  - <code>locations.py</code>

Cada una tiene su constructor y un método que convierte los parámetros a formato json

## Querys

### db.COLLECTION.find()

Esta query se ha usado para obtener todos los documentos de la colección, por ejemplo, en la **línea 83** del archivo **characters.py**:

```python
characters = db.characters.find()
```

### db.COLLECTION.find_one(filter,**kwargs)

Esta query se ha usado para saber si la colección está vacía, de tal manera que se muestre el botón para insertar los datos. Pero su función principal es realizar la búsqueda por un filtro, como en el siguiente caso (**línea 94** del archivo **characters.py**):

```python
name_episode = db.episodes.find_one({"idE": int(episode["id_episode"])}, {"name": 1})["name"]
```
En donde extraemos el nombre de un capítulo.

### db.COLLECTION.insert_one(json)

Esta query se ha usado para insertar un documento en la colección, agregando así los datos de los personajes, episodios y locaciones. Por ejemplo, en la **línea 41** del archivo **characters.py**:

```python
db.characters.insert_one(character.to_json())
```
Se inserta una instacia a la colección characters.

### db.COLLECTION.update_one(filter, new_values)

Esta query se ha usado para actualizar los valores de las claves:
- <code>name_episode</code> del campo <code>list_episodes</code> en la colección <code>characters</code>
- <code>name_character</code> del campo <code>list_characters</code> en la colección <code>episodes</code>
- <code>name_character</code> del campo <code>list_characters</code> en la colección <code>locations</code>.

Por ejemplo, en la **línea 95** del archivo **characters.py**:

```python
db.characters.update_one({"idRM": idch}, {"$set": {"list_episodes." + str(count) + ".name_episode": name_episode}})
```

### db.COLLECTION.find().sort(field, order)

Esta query permite ordenar los datos de acuerdo a un campo seleccionado de manera ascendente (default) 1 o descendente -1, por ejemplo en la **línea 139** del archivo **characters.py**:

```python
characters = db.characters.find().sort("idRM", -1)
```

## Insertar personajes
    
Para obtener todos los datos es necesario ejecutar toda la función <code>insertDB</code>
https://github.com/WilliamMiguel/RickAndMortyAPI/blob/a425109e025e7e665440eee24bdac7c77f58e569/app/routes/characters.py#L19
