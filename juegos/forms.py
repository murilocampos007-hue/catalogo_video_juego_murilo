from django import forms
from .models import Juego, Franquicia, Resena, Perfil
import re

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'desarrollador', 'distribuidor', 'franquicia', 
        'generos', 'plataformas', 'fecha_lanzamiento', 'descripcion', 'imagen'
        ]

    def clean_titulo(self):
        verificacion_juego = self.cleaned_data['titulo']
        padron = re.compile(r"^\w")
        texto = padron.match(verificacion_juego)
        if texto == None:
            raise forms.ValidationError("Titulo tiene que empezar con un número o letra.")
        return verificacion_juego


class FranquiciaForm(forms.ModelForm):
    class Meta:
        model = Franquicia
        fields = ['nombre', 'descripcion', 'imagen'
        ]

    def clean_nombre(self):
        verificacion_franquicia = self.cleaned_data['nombre']
        padron = re.compile(r"^\w")
        texto = padron.match(verificacion_franquicia)
        if texto == None:
            raise forms.ValidationError("Nombre tiene que empezar con un número o letra.")
        return verificacion_franquicia


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['puntuacion', 'comentario',
        ]


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto', 'biografia', 'pais', 'juego_favorito', 'plataforma_favorita',
        ]

    def clean_nombre(self):
        verificacion_franquicia = self.cleaned_data['nombre']
        padron = re.compile(r"^\w")
        texto = padron.match(verificacion_franquicia)
        if texto == None:
            raise forms.ValidationError("Nombre tiene que empezar con un número o letra.")
        return verificacion_franquicia