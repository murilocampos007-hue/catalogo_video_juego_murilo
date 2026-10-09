"""
URL configuration for catalogo_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from juegos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mirar_catalogo, name='inicio'),
    path('catalogo/', views.mirar_catalogo, name='catalogo'),
    path('franquicias/<int:id_franquicia>/', views.mirar_franquicia, name='detalle_franquicia'),
    path('juegos/<int:id_juego>/', views.mirar_ficha, name='detalle_juego'),
    path('juegos/nuevo/', views.crear_juego, name='crear_juego'),
    path('juegos/editar/<int:id_juego>/', views.editar_juego, name='editar_juego'),
    path('juegos/borrar/<int:id_juego>/', views.borrar_juego, name='borrar_juego'),
    path('franquicias/nuevo/', views.crear_franquicia, name='crear_franquicia'),
    path('franquicias/editar/<int:id_franquicia>/', views.editar_franquicia, name='editar_franquicia'),
    path('franquicias/borrar/<int:id_franquicia>/', views.borrar_franquicia, name='borrar_franquicia'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.crear_cuenta, name='registro'),
    path('resenas/nueva/<int:id_juego>/', views.crear_resena, name='crear_resena'),
    path('resenas/editar/<int:id_resena>/', views.editar_resena, name='editar_resena'),
    path('resenas/borrar/<int:id_resena>/', views.borrar_resena, name='borrar_resena'),
    path('perfiles/<int:id_usuario>/', views.ver_perfil, name='ver_perfil'),
    path('perfiles/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfiles/borrar/', views.borrar_perfil, name='borrar_perfil'),
    path('gestion/', views.gestion, name='gestion')
]
