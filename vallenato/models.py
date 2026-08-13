from django.db import models


class Artista(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True)
    imagen = models.CharField(max_length=120)
    apodo = models.CharField(max_length=120)
    origen = models.CharField(max_length=160)
    anio_inicio = models.PositiveIntegerField()
    reproducciones = models.PositiveIntegerField(help_text="Reproducciones en millones")
    destacado = models.BooleanField(default=False)
    descripcion = models.TextField()

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Cancion(models.Model):
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name="canciones",
    )
    titulo = models.CharField(max_length=160)
    anio = models.PositiveIntegerField()

    class Meta:
        ordering = ["anio", "titulo"]

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"
