from django.shortcuts import render, get_object_or_404
from .models import Juego

# Create your views here.

def mirar_catalogo(request):
    todos_los_juegos = Juego.objetcs.all()
    return render(request, 'catalogo.html', {})