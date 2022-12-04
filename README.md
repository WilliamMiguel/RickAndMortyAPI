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

### Insertando los personajes

Luego acceder al localhost: http://127.0.0.1:5000/ y hacer click en **Insertar personajes** para crear la base de datos, posteriormente no se mostrará esta opción. De esta forma se cargan todos los personajes, episodios y locaciones.

La función <code>insertDB</code> realiza este procedimiento mediante los siguientes pasos:
1. Crea la colección <code>characters</code>.
2. Crea la colección <code>episodes</code>.
3. Crea la colección <code>locations</code>.
4. En la colección <code>characters</code>, se rellena la clave <code>name_episode</code> del campo <code>list_episodes</code>
5. En la colección <code>episodes</code>, se rellena la clave <code>name_character</code> del campo <code>list_characters</code>
6. En la colección <code>locations</code>, se rellena la clave <code>name_character</code> del campo <code>list_characters</code>

Primero se crean las 3 colecciones para evitar realizar <code>requests</code> en cada personaje debido a que el tiempo de espera se extiende. Posteriormente se rellenan los campos trayendo los datos necesarios de cada colección.
