# Rick and Morty - MongoDB

Trabajando con bases de datos no relacionales y Flask. Se muestran los personajes y un enlace a su perfil con algunos datos.

## Instalación
Crear una carpeta e inicia VS Code dentro de ella, luego crear el entorno virtual ejecutando la siguiente línea:

```bash
py -m venv env
```
Acceder al entorno virtual y activarlo. En Windows:

```bash
.\env\scripts\activate
```

Instalar las dependencias que se encuentran en requirements.txt

```bash
pip install -r requirements.txt
```

## Uso
Ejecutar la siguiente línea de código dentro del entorno virtual
```python
flask run
```
Luego acceder al localhost: http://127.0.0.1:5000/

## Insertar personajes
Para cambiar la cantidad de páginas de las cuales se extrae el personaje se debe modificar la **línea 16** del archivo **characters.py** ubicado en la **carpeta app**

```python
#for page in range ("desde la página 1, hasta la página 21")
for page in range (1,22)
```
