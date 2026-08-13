from django.contrib import admin

from .models import Artista, Cancion


class CancionInline(admin.TabularInline):
    model = Cancion
    extra = 0


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "origen", "anio_inicio", "reproducciones", "destacado")
    list_filter = ("destacado", "anio_inicio")
    prepopulated_fields = {"slug": ("nombre",)}
    search_fields = ("nombre", "apodo", "origen")
    inlines = [CancionInline]


@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "artista", "anio")
    list_filter = ("anio", "artista")
    search_fields = ("titulo", "artista__nombre")
