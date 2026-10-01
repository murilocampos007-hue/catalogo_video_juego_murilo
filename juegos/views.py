from django.shortcuts import render, get_object_or_404
from .models import Franquicia

# Create your views here.

def mirar_catalogo(request):
    """Listado de franquicias y enseña todo en una única página."""
    todas_las_franquicias = Franquicia.objects.all()
    return render(request, 'catalogo.html', {'franquicias': todas_las_franquicias})


def mirar_franquicia(request, id_franquicia):
    franquicia_seleccionada = get_object_or_404(Franquicia, id=id_franquicia)
    return render(request, 'detalle_franquicias.html', {'franquicia': franquicia_seleccionada})