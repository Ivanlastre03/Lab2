# Lab2 en Django

## Informacion del estudiante

**Nombre:** Ivan Lastre  
**ID:** 000524727

## Descripcion del proyecto

Este proyecto es una pagina web desarrollada con Django para el Lab 2. La pagina presenta una coleccion dinamica de artistas representativos del vallenato colombiano. En la pantalla principal se muestra una introduccion del proyecto, una seccion informativa, una lista de canciones recomendadas y un listado de artistas generado desde datos enviados por la vista de Django.

Cada artista tiene informacion propia como nombre, origen, apodo, descripcion, imagen, anio de inicio, reproducciones y una lista interna de canciones. Desde el listado principal se puede entrar a una pagina de detalle individual usando una ruta dinamica. En esa vista se muestra la informacion completa del artista seleccionado y sus canciones representativas.

El objetivo del proyecto es demostrar el uso de un motor de plantillas, datos dinamicos, estructuras anidadas, rutas de detalle, condicionales, HTML5 semantico y estilos con CSS/Flexbox.

## Tecnologias utilizadas

- Python
- Django 5.0.7
- HTML5
- CSS3
- JavaScript
- Django Templates

## Como ejecutar el proyecto

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el servidor local:

```bash
py manage.py runserver localhost:8000
```

Abrir en el navegador:

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

El proyecto usa el motor de plantillas de Django. Las paginas HTML no son archivos estaticos solamente, sino plantillas que reciben datos desde Python y los muestran en el navegador.

Esto se evidencia en:

- `templates/base.html`
- `templates/index.html`
- `templates/detalle.html`
- `vallenato/views.py`

Se usan instrucciones propias de Django Templates como:

- `{% extends %}`
- `{% block %}`
- `{% for %}`
- `{% if %}`
- `{{ variable }}`
- `{% static %}`

### 2. Coleccion de datos

La coleccion principal esta en `vallenato/views.py` y se llama `ARTISTAS`. Esta coleccion contiene 4 artistas:

- Diomedes Diaz
- Poncho Zuleta
- Jorge Oñate
- Silvestre Dangond

Cada artista tiene varios campos, por ejemplo:

- `nombre`
- `slug`
- `imagen`
- `apodo`
- `origen`
- `anio_inicio`
- `reproducciones`
- `destacado`
- `descripcion`
- `canciones`

### 3. Datos anidados y campo numerico

Cada artista tiene una lista interna llamada `canciones`. Esa lista es un dato anidado porque esta dentro de cada elemento de la coleccion principal.

Ejemplo de estructura usada:

```python
"canciones": [
    {"titulo": "Bonita", "anio": 1988},
    {"titulo": "Sin medir distancias", "anio": 1986},
]
```

Tambien se usan campos numericos como:

- `anio_inicio`
- `anio`
- `reproducciones`

Estos valores se muestran en la pagina principal y en la pagina de detalle.

### 4. Layout compartido

El archivo `templates/base.html` funciona como layout compartido. Alli se encuentra la estructura comun del sitio:

- `head`
- enlaces a CSS
- barra de navegacion
- bloque principal de contenido
- footer
- enlace al JavaScript

Las demas paginas reutilizan ese layout con:

```django
{% extends "base.html" %}
```

### 5. Listado generado con bucle

El listado de artistas no esta escrito manualmente en HTML. Se genera con un bucle en `templates/index.html`:

```django
{% for artista in artistas %}
```

Gracias a ese bucle, Django recorre la coleccion `ARTISTAS` y crea una tarjeta por cada artista.

### 6. Rutas dinamicas de detalle

El proyecto tiene una ruta dinamica para ver el detalle de cada artista:

```python
path("artistas/<slug:slug>/", views.detalle_artista, name="detalle_artista")
```

Cada tarjeta del listado tiene un enlace a su detalle usando el `slug` del artista. Por ejemplo:

- `/artistas/diomedes-diaz/`
- `/artistas/poncho-zuleta/`
- `/artistas/jorge-onate/`
- `/artistas/silvestre-dangond/`

### 7. Condicional en plantilla

La pagina usa un condicional para mostrar si un artista esta marcado como destacado.

En `templates/index.html` y `templates/detalle.html` se usa:

```django
{% if artista.destacado %}
```

Si el artista esta destacado, se muestra una etiqueta especial. Si no lo esta, en la pagina de detalle se muestra una etiqueta alternativa.

### 8. HTML5 semantico

La pagina usa etiquetas semanticas de HTML5 para organizar mejor el contenido:

- `header`
- `nav`
- `main`
- `section`
- `article`
- `footer`

Esto hace que la estructura de la pagina sea mas clara y correcta.

### 9. Flexbox y estilos

El archivo `static/styles.css` contiene los estilos visuales del proyecto. Se usa Flexbox en varias partes de la pagina, como:

- barra de navegacion
- seccion hero
- tarjetas de artistas
- estadisticas
- elementos de detalle

Tambien se usan estilos responsivos para que la pagina se adapte a diferentes tamanos de pantalla.

### 10. README y calidad del repositorio

Este README documenta:

- autor e ID
- descripcion del proyecto
- tecnologias usadas
- instrucciones de ejecucion
- rutas disponibles
- explicacion de cada entregable del Lab 2

El repositorio tambien incluye un archivo `.gitignore` para evitar subir archivos innecesarios como bases de datos locales, cache de Python y entornos virtuales.

## Verificacion

El proyecto fue verificado con:

```bash
py manage.py check
py manage.py test
```

Ambas verificaciones pasan correctamente.
