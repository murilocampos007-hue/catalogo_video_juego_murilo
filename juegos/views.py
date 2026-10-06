from django.shortcuts import render, get_object_or_404, redirect
from .models import Franquicia, Juego
from .forms import JuegoForm, FranquiciaForm
import logging
import re
logger = logging.getLogger(__name__)

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


def crear_juego(request):
    if request.method == "POST":
        form = JuegoForm(request.POST)
        if form.is_valid():
            try:
                juego = form.save()
                logger.info(f"El Juego {juego.titulo} se creó con éxito.")
                return redirect ('detalle_juego', id_juego=juego.id)

            except Exception:
                logger.exception("Error en añadir Juego.")
                form.add_error(None, "No se pudio añadir el Juego al Sistema.")

    else:
        form = JuegoForm()
    return render(request, 'formulario.html', {'form': form})


def editar_juego(request, id_juego):
    juego = get_object_or_404(Juego, id=id_juego)
    if request.method == "POST":
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            try:
                editor = form.save()
                logger.info(f"El Juego {editor.titulo} se editó con éxito.")
                return redirect('detalle_juego', id_juego=juego.id)

            except Exception:
                logger.exception("Error al editar Juego.")
                form.add_error(None, "No se pudio editar el Juego.")

    else:
        form = JuegoForm(instance=juego)
    return render(request, 'formulario.html', {'form': form})


def borrar_juego(request, id_juego):
    juego_del = get_object_or_404(Juego, id=id_juego)
    if request.method == "POST":
        try:
            juego_del.delete()
            logger.info(f"El Juego {juego_del.titulo} se borró con éxito.")
            return redirect ('catalogo')
           
    
        except Exception:
            logger.exception("Error al borrar el Juego.")
    return render(request, 'confirmar_borrado.html', {'juego': juego_del})



def crear_franquicia(request):
    if request.method == "POST":
        form = FranquiciaForm(request.POST)
        if form.is_valid():
            try:
                franquicia = form.save()
                logger.info(f"La Franquicia {Franquicia.nombre} se creó con éxito.")
                return redirect ('detalle_franquicia', id_franquicia=franquicia.id)

            except Exception:
                logger.exception("Error en añadir Franquicia.")
                form.add_error(None, "No se pudio añadir la Franquicia al Sistema.")

    else:
        form = FranquiciaForm()
    return render(request, 'formulario.html', {'form': form})


def editar_franquicia(request, id_franquicia):
    franquicia = get_object_or_404(Franquicia, id=id_franquicia)
    if request.method == "POST":
        form = FranquiciaForm(request.POST, instance=franquicia)
        if form.is_valid():
            try:
                editor = form.save()
                logger.info(f"La Franquicia {editor.nombre} se editó con éxito.")
                return redirect('detalle_franquicia', id_franquicia=franquicia.id)

            except Exception:
                logger.exception("Error al editar la Franquicia.")
                form.add_error(None, "No se pudio editar la Franquicia.")

    else:
        form = FranquiciaForm(instance=franquicia)
    return render(request, 'formulario.html', {'form': form})


def borrar_franquicia(request, id_franquicia):
    franquicia_del = get_object_or_404(Franquicia, id=id_franquicia)
    if request.method == "POST":
        try:
            franquicia_del.delete()
            logger.info(f"La Franquicia{franquicia_del.nombre} se borró con éxito.")
            return redirect ('catalogo')
    
        except Exception:
            logger.exception("Error al borrar la Franquicia.")
    return render(request, 'borrar_franquicia.html', {'franquicia': franquicia_del})
