from django.shortcuts import render, get_object_or_404
from .models import Juego

# Create your views here.

def mirar_catalogo(request):
    """Listado de juegos y enseña todo en una única página."""
    todos_los_juegos = Juego.objects.all()
    return render(request, 'catalogo.html', {'juegos': todos_los_juegos})