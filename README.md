# Lab2 en Django

**Nombre:** Ivan Lastre  
**ID:** 000524727

## Descripcion del proyecto

Este proyecto es una pagina web desarrollada con Django para el Lab 2. La pagina presenta una coleccion dinamica de artistas representativos del vallenato colombiano. En la pantalla principal se muestra una introduccion del proyecto, una seccion informativa, una lista de canciones recomendadas y un listado de artistas generado desde datos enviados por la vista de Django.

Cada artista tiene informacion propia como nombre, origen, apodo, descripcion, imagen, anio de inicio, reproducciones y una lista interna de canciones. Desde el listado principal se puede entrar a una pagina de detalle individual usando una ruta dinamica. En esa vista se muestra la informacion completa del artista seleccionado y sus canciones representativas.

El proyecto tambien queda preparado para conectarse a PostgreSQL usando variables de entorno, evitando guardar contrasenas dentro del codigo.

## Tecnologias utilizadas

- Python
- Django 5.0.7
- PostgreSQL
- psycopg
- python-dotenv
- HTML5
- CSS3
- JavaScript
- Django Templates

## Instalacion

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuracion de PostgreSQL

Primero crea una base de datos en PostgreSQL. Puedes llamarla:

```text
lab2_django
```

Luego crea un archivo llamado `.env` en la raiz del proyecto. Puedes copiar el archivo `.env.example` y cambiar la contrasena por la de tu PostgreSQL:

```text
USE_POSTGRES=True
POSTGRES_DB=lab2_django
POSTGRES_USER=postgres
POSTGRES_PASSWORD=tu_contrasena
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

Despues ejecuta las migraciones para crear las tablas internas de Django en PostgreSQL:

```bash
py manage.py migrate
```

Si todavia no quieres usar PostgreSQL, deja `USE_POSTGRES=False` o no crees el archivo `.env`. En ese caso Django usara SQLite como respaldo local.

## Ejecucion del proyecto

Ejecuta el servidor local:

```bash
py manage.py runserver localhost:8000
```

Abre en el navegador:

```text
http://localhost:8000/
```

## Rutas principales

- `/`: pagina principal con informacion general, playlist y listado de artistas.
- `/artistas/<slug>/`: pagina dinamica de detalle para cada artista.

Ejemplo:

```text
http://localhost:8000/artistas/diomedes-diaz/
```

## Entregables del Lab 2 aplicados a la pagina

### 1. Motor de plantillas

El proyecto usa el motor de plantillas de Django. Las paginas HTML reciben datos desde Python y los muestran en el navegador.

Se usan instrucciones como:

- `{% extends %}`
- `{% block %}`
- `{% for %}`
- `{% if %}`
- `{{ variable }}`
- `{% static %}`

### 2. Coleccion de datos

La coleccion principal esta en `vallenato/views.py` y se llama `ARTISTAS`. Contiene 4 artistas:

- Diomedes Diaz
- Poncho Zuleta
- Jorge Oñate
- Silvestre Dangond

Cada artista tiene campos como `nombre`, `slug`, `imagen`, `apodo`, `origen`, `anio_inicio`, `reproducciones`, `destacado`, `descripcion` y `canciones`.

### 3. Datos anidados y campos numericos

Cada artista tiene una lista interna llamada `canciones`. Esa lista es un dato anidado porque esta dentro de cada elemento de la coleccion principal.

Tambien se usan campos numericos como:

- `anio_inicio`
- `anio`
- `reproducciones`

### 4. Layout compartido

El archivo `templates/base.html` funciona como layout compartido. Alli se encuentra la estructura comun del sitio: `head`, navegacion, bloque principal, footer, CSS y JavaScript.

Las demas paginas reutilizan ese layout con:

```django
{% extends "base.html" %}
```

### 5. Listado generado con bucle

El listado de artistas se genera con un bucle en `templates/index.html`:

```django
{% for artista in artistas %}
```

Django recorre la coleccion `ARTISTAS` y crea una tarjeta por cada artista.

### 6. Rutas dinamicas de detalle

El proyecto tiene una ruta dinamica para ver el detalle de cada artista:

```python
path("artistas/<slug:slug>/", views.detalle_artista, name="detalle_artista")
```

Ejemplos:

- `/artistas/diomedes-diaz/`
- `/artistas/poncho-zuleta/`
- `/artistas/jorge-onate/`
- `/artistas/silvestre-dangond/`

### 7. Condicional en plantilla

La pagina usa un condicional para mostrar si un artista esta marcado como destacado:

```django
{% if artista.destacado %}
```

Si el artista esta destacado, se muestra una etiqueta especial. Si no lo esta, en la pagina de detalle se muestra una etiqueta alternativa.

### 8. HTML5 semantico

La pagina usa etiquetas semanticas como:

- `header`
- `nav`
- `main`
- `section`
- `article`
- `footer`

### 9. Flexbox y estilos

El archivo `static/styles.css` contiene los estilos visuales del proyecto. Se usa Flexbox en la navegacion, el hero, las tarjetas, las estadisticas y los elementos de detalle.

### 10. Base de datos PostgreSQL

Django esta configurado para usar PostgreSQL cuando `USE_POSTGRES=True` en el archivo `.env`. La configuracion esta en `vallenato_project/settings.py` y lee estos valores:

- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

Si `USE_POSTGRES` no esta activo, el proyecto usa SQLite para facilitar pruebas locales.

## Verificacion

El proyecto fue verificado con:

```bash
py manage.py check
py manage.py test
```

Para verificar PostgreSQL despues de configurar `.env`, ejecuta:

```bash
py manage.py migrate
```

Si la base de datos, usuario y contrasena son correctos, Django creara las tablas sin errores.
