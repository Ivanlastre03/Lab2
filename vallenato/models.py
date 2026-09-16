from mongoengine import (
    Document,
    StringField,
    IntField,
    BooleanField,
)


class Artista(Document):
    nombre = StringField(required=True, max_length=120)
    slug = StringField(required=True, unique=True)
    apodo = StringField(max_length=120)
    origen = StringField(max_length=150)
    descripcion = StringField()
    imagen = StringField()

    anio_inicio = IntField()
    reproducciones = IntField(default=0)

    destacado = BooleanField(default=False)

    meta = {
        "collection": "artistas"
    }

    def __str__(self):
        return self.nombre