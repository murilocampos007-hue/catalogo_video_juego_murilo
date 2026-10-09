from django import forms
from .models import Juego, Franquicia, Resena, Perfil
import re


class FormularioCatalogo(forms.ModelForm):
    """Base de los formularios de juegos y franquicias."""
    def comprobar_inicio(self, texto):
        """Mira si el texto empieza por letra o número. Si no, da error."""
        padron = re.compile(r"^\w")
        verificar = padron.match(texto)
        if verificar == None:
            raise forms.ValidationError("Tiene que empezar con un número o letra.")
        return texto


class JuegoForm(FormularioCatalogo):
    """Formulario de juegos."""
    class Meta:
        model = Juego
        fields = ['titulo', 'desarrollador', 'distribuidor', 'franquicia', 
        'generos', 'plataformas', 'fecha_lanzamiento', 'descripcion', 'imagen'
        ]

    def clean_titulo(self):
        """Valida el título con comprobar_inicio."""
        verificacion_juego = self.cleaned_data['titulo']
        return self.comprobar_inicio(verificacion_juego)


class FranquiciaForm(FormularioCatalogo):
    """Formulario para las franquicias."""
    class Meta:
        model = Franquicia
        fields = ['nombre', 'descripcion', 'imagen'
        ]

    def clean_nombre(self):
        """Lo mismo que clean_titulo, pero con el nombre."""
        verificacion_franquicia = self.cleaned_data['nombre']
        return self.comprobar_inicio(verificacion_franquicia)


class ResenaForm(forms.ModelForm):
    """Formulario de reseñas. Solo pide puntuación y comentario.""" 
    class Meta:
        model = Resena
        fields = ['puntuacion', 'comentario',
        ]
        widgets = {
            'puntuacion': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }


class PerfilForm(forms.ModelForm):
    """Para que cada usuario edite su perfil."""
    class Meta:
        model = Perfil
        fields = ['foto', 'biografia', 'pais', 'juego_favorito', 'plataforma_favorita',
        ]


