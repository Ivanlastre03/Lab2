from django.shortcuts import get_object_or_404, render

from .models import Artista


def index(request):
    artistas = Artista.objects.prefetch_related("canciones").all()
    total_canciones = sum(artista.canciones.count() for artista in artistas)

    return render(
        request,
        "index.html",
        {
            "artistas": artistas,
            "total_canciones": total_canciones,
        },
    )


def detalle_artista(request, slug):
    artista = get_object_or_404(
        Artista.objects.prefetch_related("canciones"),
        slug=slug,
    )
    return render(request, "detalle.html", {"artista": artista})
