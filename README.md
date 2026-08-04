# Lab2 en Django

Proyecto web academico construido con Django para presentar una coleccion dinamica de artistas representativos del vallenato colombiano.

## Requisitos

- Python 3.10 o superior
- Django 5.0.7

Instalacion de dependencias:

```bash
pip install -r requirements.txt
```

Ejecucion del proyecto:

```bash
py manage.py runserver
```

Luego abre:

```text
http://127.0.0.1:8000/
```

## Rutas

- `/`: listado principal de artistas.
- `/artistas/<slug>/`: pagina de detalle dinamica para cada artista.

## Cumplimiento Lab 2

- Motor de plantillas: usa Django Templates con `extends`, `block`, `for`, `if`, variables y `static`.
- Coleccion de datos: la lista `ARTISTAS` contiene 4 artistas, campos numericos y datos anidados en `canciones`.
- Layout compartido: `templates/base.html` centraliza `head`, navegacion, footer, CSS y JavaScript.
- Listado con bucle: `templates/index.html` recorre `artistas` con `{% for artista in artistas %}`.
- Rutas dinamicas: `vallenato/urls.py` define `artistas/<slug:slug>/`.
- Condicional: las plantillas muestran una etiqueta diferente segun `artista.destacado`.
- HTML5 semantico: usa `header`, `nav`, `main`, `section`, `article` y `footer`.
- Flexbox: el CSS usa Flexbox en navegacion, hero, tarjetas y secciones de estadisticas.

## Autor

Ivan Lastre
