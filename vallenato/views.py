import json

from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from mongoengine.errors import ValidationError, NotUniqueError

from .models import Artista

def artista_a_dict(artista):
    return {
        "id": str(artista.id),
        "nombre": artista.nombre,
        "slug": artista.slug,
        "apodo": artista.apodo,
        "origen": artista.origen,
        "descripcion": artista.descripcion,
        "imagen": artista.imagen,
        "anio_inicio": artista.anio_inicio,
        "reproducciones": artista.reproducciones,
        "destacado": artista.destacado,
    }

def index(request):
    artistas = Artista.objects.order_by("nombre")

    return render(
        request,
        "index.html",
        {
            "artistas": artistas,
            "total_canciones": 0,
        },
    )

def detalle_artista(request, slug):
    artista = Artista.objects(slug=slug).first()

    if not artista:
        raise Http404("Artista no encontrado")

    return render(
        request,
        "detalle.html",
        {
            "artista": artista
        },
    )

@csrf_exempt
def crear_artista(request):

    if request.method != "POST":
        return JsonResponse(
            {"error": "Metodo no permitido"},
            status=405
        )

    try:
        datos = json.loads(request.body)

        artista = Artista(
            nombre=datos.get("nombre"),
            slug=datos.get("slug"),
            apodo=datos.get("apodo", ""),
            origen=datos.get("origen", ""),
            descripcion=datos.get("descripcion", ""),
            imagen=datos.get("imagen", ""),
            anio_inicio=datos.get("anio_inicio"),
            reproducciones=datos.get("reproducciones", 0),
            destacado=datos.get("destacado", False),
        )

        artista.save()

        return JsonResponse(
            {
                "mensaje": "Artista creado correctamente",
                "artista": artista_a_dict(artista),
            },
            status=201
        )

    except NotUniqueError:
        return JsonResponse(
            {"error": "Ya existe un artista con ese slug"},
            status=400
        )

    except (ValidationError, ValueError, TypeError) as error:
        return JsonResponse(
            {"error": str(error)},
            status=400
        )

def listar_artistas(request):

    if request.method != "GET":
        return JsonResponse(
            {"error": "Metodo no permitido"},
            status=405
        )

    artistas = Artista.objects.order_by("nombre")

    lista = [
        artista_a_dict(artista)
        for artista in artistas
    ]

    return JsonResponse(
        lista,
        safe=False
    )

@csrf_exempt
def actualizar_artista(request, id):

    if request.method != "PUT":
        return JsonResponse(
            {"error": "Metodo no permitido"},
            status=405
        )

    try:
        artista = Artista.objects(id=id).first()

        if not artista:
            return JsonResponse(
                {"error": "Artista no encontrado"},
                status=404
            )

        datos = json.loads(request.body)

        campos_permitidos = [
            "nombre",
            "slug",
            "apodo",
            "origen",
            "descripcion",
            "imagen",
            "anio_inicio",
            "reproducciones",
            "destacado",
        ]

        for campo in campos_permitidos:
            if campo in datos:
                setattr(artista, campo, datos[campo])

        artista.save()

        return JsonResponse(
            {
                "mensaje": "Artista actualizado correctamente",
                "artista": artista_a_dict(artista),
            }
        )

    except NotUniqueError:
        return JsonResponse(
            {"error": "Ya existe otro artista con ese slug"},
            status=400
        )

    except (ValidationError, ValueError, TypeError) as error:
        return JsonResponse(
            {"error": str(error)},
            status=400
        )


@csrf_exempt
def eliminar_artista(request, id):

    if request.method != "DELETE":
        return JsonResponse(
            {"error": "Metodo no permitido"},
            status=405
        )

    try:
        artista = Artista.objects(id=id).first()

        if not artista:
            return JsonResponse(
                {"error": "Artista no encontrado"},
                status=404
            )

        nombre = artista.nombre

        artista.delete()

        return JsonResponse(
            {
                "mensaje": f"Artista {nombre} eliminado correctamente"
            }
        )

    except ValidationError:
        return JsonResponse(
            {"error": "ID invalido"},
            status=400
        )