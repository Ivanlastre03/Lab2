from django.db import migrations


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
            {"titulo": "Tu eres la reina", "anio": 1978},
            {"titulo": "Sin medir distancias", "anio": 1986},
            {"titulo": "Bonita", "anio": 1988},
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
            {"titulo": "Mi hermano y yo", "anio": 1974},
            {"titulo": "La sangre llama", "anio": 1980},
            {"titulo": "Ni pio", "anio": 1992},
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
            {"titulo": "Se te fueron las luces", "anio": 1975},
            {"titulo": "Una aventura", "anio": 1978},
            {"titulo": "Nunca comprendi tu amor", "anio": 1982},
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
            {"titulo": "La gringa", "anio": 2017},
            {"titulo": "Que no se enteren", "anio": 2020},
        ],
    },
]


def cargar_artistas(apps, schema_editor):
    Artista = apps.get_model("vallenato", "Artista")
    Cancion = apps.get_model("vallenato", "Cancion")

    for datos in ARTISTAS:
        canciones = datos.pop("canciones")
        artista, _ = Artista.objects.update_or_create(
            slug=datos["slug"],
            defaults=datos,
        )

        for cancion in canciones:
            Cancion.objects.update_or_create(
                artista=artista,
                titulo=cancion["titulo"],
                defaults={"anio": cancion["anio"]},
            )


def borrar_artistas(apps, schema_editor):
    Artista = apps.get_model("vallenato", "Artista")
    Artista.objects.filter(slug__in=[artista["slug"] for artista in ARTISTAS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("vallenato", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(cargar_artistas, borrar_artistas),
    ]
