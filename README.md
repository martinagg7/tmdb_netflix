# tmdb_netflix
# Proyecto Web NetflixUAX

Este proyecto es una **web desarrollada en Django** que simula una plataforma similar a Netflix. Permite explorar películas y series, además de gestionar favoritos. Fue desarrollado como parte de un aprendizaje práctico de desarrollo web.

---

## Estructura del Repositorio

La estructura del proyecto es la siguiente:

```plaintext
.
├── manage.py
├── requirements.txt
├── .gitignore
├── netflixuax/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   ├── authentication/
│   │   ├── migrations/
│   │   ├── templates/
│   ├── streaming/
│   │   ├── migrations/
│   │   ├── static/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   ├── templates/
│   │   ├── scripts/
│   │   │   ├── peliculas.py
│   │   │   ├── series.py
 ```
## Secciones del Sitio Web

### 1. **Home**
La **página principal** del sitio web, donde se presentan las secciones más relevantes, como las películas más populares y las series mejor valoradas.

### 2. **Películas**
Incluye las siguientes subcategorías:
- **Now Playing:** Lista de películas que actualmente están en cartelera.
- **Top Rated:** Películas con mejores calificaciones según la API de TMDb.

### 3. **Series**
Incluye las siguientes subcategorías:
- **Series Populares:** Series que tienen mayor popularidad en la API de TMDb.
- **Series Hoy:** Episodios de series que se emiten en el día actual.

### 4. **Favoritos**
Permite al usuario **guardar y consultar sus películas y series favoritas** en su perfil personal.

### 5. **Buscar**
Un buscador para encontrar películas y series específicas utilizando palabras clave.

### 6. **Perfil**
Una sección personalizada para el usuario registrado, donde puede gestionar sus datos y acceder a sus favoritos.

## Ejecución 

    1.Clona el repositorio desde GitHub y accede a la carpeta del proyecto
    git clone https://github.com/martinagg7/tmdb_netflix.git
    cd netflixuax
    
    2.Crea un entorno virtual para aislar las dependencias del proyecto y actívalo
    python -m venv env-django
    source env-django/bin/activate  
    
    3.Instala las dependencias necesarias desde el archivo requirements.txt
    pip install -r requirements.txt
    
    Aplica las migraciones de la base de datos
    python manage.py migrate
    
    5.Ejecuta el servidor de desarrollo local
    python manage.py runserver
## Desplegar el Proyecto

Para desplegar este proyecto en **Vercel**, se configuró una base de datos en **PostgreSQL** para permitir el almacenamiento de las películas favoritas.

## Datos Repositorio
Nombre Usuario: @martinagg7

Link Repositorio https://github.com/martinagg7/tmdb_netflix.git
