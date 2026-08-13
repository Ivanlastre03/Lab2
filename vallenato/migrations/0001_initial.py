from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Artista",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=120)),
                ("slug", models.SlugField(max_length=140, unique=True)),
                ("imagen", models.CharField(max_length=120)),
                ("apodo", models.CharField(max_length=120)),
                ("origen", models.CharField(max_length=160)),
                ("anio_inicio", models.PositiveIntegerField()),
                ("reproducciones", models.PositiveIntegerField(help_text="Reproducciones en millones")),
                ("destacado", models.BooleanField(default=False)),
                ("descripcion", models.TextField()),
            ],
            options={
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Cancion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=160)),
                ("anio", models.PositiveIntegerField()),
                (
                    "artista",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="canciones",
                        to="vallenato.artista",
                    ),
                ),
            ],
            options={
                "ordering": ["anio", "titulo"],
            },
        ),
    ]
