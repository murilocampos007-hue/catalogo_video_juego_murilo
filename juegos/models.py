from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ElementoCatalogo(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True


class Empresa(ElementoCatalogo):
    """Empresa que desarrolla o distribuye juegos."""
    pass

    

class Franquicia(ElementoCatalogo):
    """Franquicia de juegos."""
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.URLField(max_length=500)


    
class Genero(ElementoCatalogo):
    """Géneros de videojuegos."""
    pass



class Plataforma(ElementoCatalogo):
    """Plataformas como consolas, PC o mobile."""
    pass


    
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

    @property
    def puntuacion_media(self):
        resenas = self.resena_set.all()
        if not resenas:
            return None
        
        total = 0
        for resena in resenas:
            total += resena.puntuacion
        media = total/len(resenas)
        return round(media, 2)


        
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

