from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Empresa(models.Model):
    """Empresa que desarrolla o distribuye juegos."""
    nombre = models.CharField(max_length=200, unique=True)
    director_ejecutivo = models.CharField(max_length=200, verbose_name="director ejecutivo")
    localizacion = models.CharField(max_length=200, verbose_name="localización")
    anio_fundacion = models.IntegerField(verbose_name="Año de Fundación")
    descripcion = models.TextField(verbose_name="Descripción")

    def __str__(self):
        return self.nombre

    

class Franquicia(models.Model):
    """Franquicia de juegos."""
    nombre = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.URLField(max_length=500)

    def __str__(self):
        return self.nombre

    

class Genero(models.Model):
    """Géneros de videojuegos."""
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

class Plataforma(models.Model):
    """Plataformas como consolas, PC o mobile."""
    nombre = models.CharField(max_length=200, unique=True)
    fabricante = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_lanzamiento = models.DateField(null=True, blank=True, verbose_name="Fecha de Lanzamiento")

    def __str__(self):
        return self.nombre


    
class Juego(models.Model):
    """Representa un videojuego del catálogo."""
    titulo = models.CharField(max_length=200, unique=True, verbose_name="Título")
    desarrollador = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True, related_name="juegos_desarrollados")
    distribuidor = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True, related_name="juegos_distribuidos")
    franquicia = models.ForeignKey(Franquicia, on_delete=models.SET_NULL, null=True, blank=True)
    generos = models.ManyToManyField(Genero)
    plataformas = models.ManyToManyField(Plataforma)
    fecha_lanzamiento = models.DateField(verbose_name="Fecha de Lanzamiento")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.URLField(max_length=500)

    def __str__(self):
        return self.titulo



class Resena(models.Model):
    """Reseñas por parte de los usuarios."""
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name="Puntuación")
    comentario = models.TextField()
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Reseñas"

    def __str__(self):
        return (f"{self.usuario} - {self.juego} ({self.puntuacion}/10)")



class Perfil(models.Model):
    """Perfil del usuario."""
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    biografia = models.TextField(null=True, blank=True, verbose_name="biografía")
    pais = models.CharField(max_length=15, null=True, blank=True, verbose_name="País")
    plataforma_favorita = models.ForeignKey(Plataforma, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Plataforma favorita")
    juego_favorito = models.ForeignKey(Juego, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Juego favorito")
    foto = models.URLField(max_length=500, null=True, blank=True)

    class Meta:
            verbose_name_plural = "Perfiles"

    def __str__(self):
        return f"{self.usuario}"

