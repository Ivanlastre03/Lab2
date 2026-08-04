from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artistas/<slug:slug>/", views.detalle_artista, name="detalle_artista"),
]
