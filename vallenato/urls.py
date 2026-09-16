from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path(
        "artistas/<slug:slug>/",
        views.detalle_artista,
        name="detalle_artista",
    ),

    path(
        "api/artistas/",
        views.listar_artistas,
        name="listar_artistas",
    ),

    path(
        "api/artistas/crear/",
        views.crear_artista,
        name="crear_artista",
    ),

    path(
        "api/artistas/<str:id>/actualizar/",
        views.actualizar_artista,
        name="actualizar_artista",
    ),

    path(
        "api/artistas/<str:id>/eliminar/",
        views.eliminar_artista,
        name="eliminar_artista",
    ),
]