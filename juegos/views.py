from django.shortcuts import render, get_object_or_404
from .models import Franquicia, Juego

# Create your views here.

def mirar_catalogo(request):
    """Listado de franquicias y enseña todo en una única página."""
    todas_las_franquicias = Franquicia.objects.all()
    return render(request, 'catalogo.html', {'franquicias': todas_las_franquicias})


def mirar_franquicia(request, id_franquicia):
    """Muestra el detalle de una franquicia y sus juegos."""
    franquicia_seleccionada = get_object_or_404(Franquicia, id=id_franquicia)
    return render(request, 'detalle_franquicias.html', {'franquicia': franquicia_seleccionada})


def mirar_ficha(request, id_juego):
    """Muestra la ficha completa de un juego."""
    juego_seleccionado = get_object_or_404(Juego, id=id_juego)
    return render(request, 'detalle_juegos.html', {'juego': juego_seleccionado})