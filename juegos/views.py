from django.shortcuts import render, get_object_or_404, redirect
from .models import Franquicia, Juego, Resena, User, Perfil
from .forms import JuegoForm, FranquiciaForm, ResenaForm, PerfilForm
import logging
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm 
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


@permission_required('juegos.add_juego', raise_exception=True)
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
                form.add_error(None, "No se pudo añadir el Juego al Sistema.")

    else:
        form = JuegoForm()
    return render(request, 'formulario.html', {'form': form})


@permission_required('juegos.change_juego', raise_exception=True)
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
                form.add_error(None, "No se pudo editar el Juego.")

    else:
        form = JuegoForm(instance=juego)
    return render(request, 'formulario.html', {'form': form})


@permission_required('delete.add_juego', raise_exception=True)
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


@permission_required('juegos.add_franquicia', raise_exception=True)
def crear_franquicia(request):
    if request.method == "POST":
        form = FranquiciaForm(request.POST)
        if form.is_valid():
            try:
                franquicia = form.save()
                logger.info(f"La Franquicia {franquicia.nombre} se creó con éxito.")
                return redirect ('detalle_franquicia', id_franquicia=franquicia.id)

            except Exception:
                logger.exception("Error en añadir Franquicia.")
                form.add_error(None, "No se pudo añadir la Franquicia al Sistema.")

    else:
        form = FranquiciaForm()
    return render(request, 'formulario.html', {'form': form})


@permission_required('juegos.change_franquicia', raise_exception=True)
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
                form.add_error(None, "No se pudo editar la Franquicia.")

    else:
        form = FranquiciaForm(instance=franquicia)
    return render(request, 'formulario.html', {'form': form})


@permission_required('juegos.delete_franquicia', raise_exception=True)
def borrar_franquicia(request, id_franquicia):
    franquicia_del = get_object_or_404(Franquicia, id=id_franquicia)
    if request.method == "POST":
        try:
            franquicia_del.delete()
            logger.info(f"La Franquicia {franquicia_del.nombre} se borró con éxito.")
            return redirect ('catalogo')
    
        except Exception:
            logger.exception("Error al borrar la Franquicia.")
    return render(request, 'borrar_franquicia.html', {'franquicia': franquicia_del})


def crear_cuenta(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                cuenta = form.save()
                logger.info(f"El perfil {cuenta.username} se creó con éxito.")
                return redirect ('login')

            except Exception:
                logger.exception("Error en crear un perfil.")
                form.add_error(None, "No se pudo añadir el perfil al Sistema.")

    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def crear_resena(request, id_juego):
    juego = get_object_or_404(Juego, id=id_juego)
    if request.method == "POST":
        form = ResenaForm(request.POST)
        if form.is_valid():
            try:
                resena = form.save(commit=False)
                resena.juego = juego
                resena.usuario = request.user
                resena.save()
                logger.info(f"La reseña de {resena.usuario} se publicó con éxito.")
                return redirect ('detalle_juego', id_juego)

            except Exception:
                logger.exception("Error en publicar reseña.")
                form.add_error(None, "No se pudo publicar la reseña.")

    else:
        form = ResenaForm()
    return render(request, 'formulario.html', {'form': form})


@login_required
def editar_resena(request, id_resena):
    resena = get_object_or_404(Resena, id=id_resena)
    if resena.usuario != request.user:
        return redirect('detalle_juego', id_juego=resena.juego.id)
    else:
        if request.method == "POST":
            form = ResenaForm(request.POST, instance=resena)
            if form.is_valid():
                try:
                    editor = form.save()
                    logger.info(f"La reseña de {editor.usuario} se editó con éxito.")
                    return redirect('detalle_juego', id_juego=resena.juego.id)

                except Exception:
                    logger.exception("Error al editar reseña.")
                    form.add_error(None, "No se pudo editar la reseña.")

        else:
            form = ResenaForm(instance=resena)
        return render(request, 'formulario.html', {'form': form})


@login_required
def borrar_resena(request, id_resena):
    resena_del = get_object_or_404(Resena, id=id_resena)
    id_juego = resena_del.juego.id
    if resena_del.usuario != request.user and not request.user.has_perm('juegos.delete_resena'):
        return redirect('detalle_juego', id_juego=id_juego)
    if request.method == "POST":
        try:
            resena_del.delete()
            logger.info(f"La reseña de {resena_del.usuario} se borró con éxito.")
            return redirect ('detalle_juego', id_juego=id_juego)
        
        except Exception:
            logger.exception("Error al borrar la reseña.")
    return render(request, 'borrar_resena.html', {'resena': resena_del})


def ver_perfil(request, id_usuario):
    usuario = get_object_or_404(User, id=id_usuario)
    perfil, creado = Perfil.objects.get_or_create(usuario=usuario)
    return render(request, 'perfil.html', {'perfil': perfil})


@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
    if request.method == "POST":
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            try:
                editor = form.save()
                logger.info(f"El Perfil {editor.usuario} se editó con éxito.")
                return redirect('ver_perfil', id_usuario=request.user.id)
    
            except Exception:
                logger.exception("Error al editar Perfil.")
                form.add_error(None, "No se pudo editar el Perfil.")
    
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'formulario.html', {'form': form})


@login_required
def borrar_perfil(request):
    perfil_del = request.user
    if request.method == "POST":
        try:
            perfil_del.delete()
            logger.info(f"La cuenta {perfil_del.username} se borró con éxito.")
            return redirect ('catalogo')
           
        except Exception:
            logger.exception("Error al borrar la cuenta.")
    return render(request, 'borrar_cuenta.html', {'perfil': perfil_del})

    

