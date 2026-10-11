# Catálogo de videojuegos RPG/JRPG

Un catálogo web de juegos RPG y JRPG hecho con Django. Los juegos van
agrupados por franquicia y cada uno tiene una ficha donde los usuarios
dejan reseñas con nota.

Está publicado en https://catalogo-video-juego-murilo.vercel.app

Lo hice como proyecto del Módulo de Python de CEI.
Murilo Campos Galindo Silva

## Qué se puede hacer

Sin cuenta se puede ver todo: catálogo, fichas y perfiles. Al registrarte
puedes escribir reseñas y editar tu perfil.

Los empleados añaden y editan juegos y franquicias desde la propia web,
sin entrar al panel de Django. Borrar solo lo hace el administrador.

## Tecnologías

Python 3.14, Django 6.1.1, SQLite en local y PostgreSQL en Vercel.
El HTML y el CSS están escritos a mano, con NES.css para los botones.

## Arrancar el proyecto en local (Windows)

    git clone https://github.com/murilocampos007-hue/catalogo_video_juego_murilo
    cd catalogo_video_juego_murilo
    python -m venv env
    env\Scripts\activate
    pip install -r requirements.txt

Hace falta un archivo .env junto a manage.py con estas dos líneas:

    LLAVE=una_clave_secreta_larga
    DEBUG=True

Y después:

    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

La base de datos empieza vacía. Las empresas, los géneros, las plataformas
y el grupo Empleados hay que crearlos desde /admin.

## Memoria técnica

El diseño de la base de datos y el porqué de cada decisión están en la
memoria técnica (PDF).