from django.db import models

# Create your models here.

class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    desarrollador = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    plataforma = models.CharField(max_length=200)
    anio_lanzamiento = models.IntegerField(verbose_name="Año de lanzamiento")
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo
