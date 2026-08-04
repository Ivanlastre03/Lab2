from django.http import Http404
from django.shortcuts import render


ARTISTAS = [
    {
        "nombre": "Diomedes Diaz",
        "slug": "diomedes-diaz",
        "imagen": "img/diomedes.jpg",
        "apodo": "El Cacique de La Junta",
        "origen": "La Junta, La Guajira",
        "anio_inicio": 1976,
        "reproducciones": 580,
        "destacado": True,
        "descripcion": (
            "Uno de los mayores referentes del vallenato colombiano, reconocido "
            "por su voz, su estilo narrativo y su influencia en varias generaciones."
        ),
        "canciones": [
            {"titulo": "Bonita", "anio": 1988},
            {"titulo": "Sin medir distancias", "anio": 1986},
            {"titulo": "Tu eres la reina", "anio": 1978},
        ],
    },
    {
        "nombre": "Poncho Zuleta",
        "slug": "poncho-zuleta",
        "imagen": "img/poncho.jpg",
        "apodo": "El Pulmon de Oro",
        "origen": "Villanueva, La Guajira",
        "anio_inicio": 1969,
        "reproducciones": 210,
        "destacado": True,
        "descripcion": (
            "Figura clave del vallenato tradicional, famoso por su fuerza vocal "
            "y por mantener vivo el sonido clasico del genero."
        ),
        "canciones": [
            {"titulo": "Ni pio", "anio": 1992},
            {"titulo": "La sangre llama", "anio": 1980},
            {"titulo": "Mi hermano y yo", "anio": 1974},
        ],
    },
    {
        "nombre": "Jorge Oñate",
        "slug": "jorge-onate",
        "imagen": "img/jorge.jpg",
        "apodo": "El Jilguero de America",
        "origen": "La Paz, Cesar",
        "anio_inicio": 1968,
        "reproducciones": 260,
        "destacado": False,
        "descripcion": (
            "Cantante historico del vallenato, recordado por su tecnica vocal "
            "y por interpretar obras esenciales del folclor colombiano."
        ),
        "canciones": [
            {"titulo": "Nunca comprendi tu amor", "anio": 1982},
            {"titulo": "Una aventura", "anio": 1978},
            {"titulo": "Se te fueron las luces", "anio": 1975},
        ],
    },
    {
        "nombre": "Silvestre Dangond",
        "slug": "silvestre-dangond",
        "imagen": "img/silvestre.jpg",
        "apodo": "Silvestrismo",
        "origen": "Urumita, La Guajira",
        "anio_inicio": 2002,
        "reproducciones": 430,
        "destacado": True,
        "descripcion": (
            "Representante moderno del vallenato, conocido por acercar el genero "
            "a nuevas audiencias con una puesta en escena contemporanea."
        ),
        "canciones": [
            {"titulo": "Mi propia historia", "anio": 2015},
            {"titulo": "Que no se enteren", "anio": 2020},
            {"titulo": "La gringa", "anio": 2017},
        ],
    },
]


def index(request):
    return render(request, "index.html", {"artistas": ARTISTAS})


def detalle_artista(request, slug):
    artista = next((artista for artista in ARTISTAS if artista["slug"] == slug), None)
    if artista is None:
        raise Http404("Artista no encontrado")

    return render(request, "detalle.html", {"artista": artista})
