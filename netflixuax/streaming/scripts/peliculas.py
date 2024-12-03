import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"

#solicitud para obtener peliculas populares
def peliculas_populares():
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,  
        "language": "es-ES",              
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener las películas populares"}

#solicitud para obtener las que están poniendo ahora
def now_playing():
    url = f"{BASE_URL}/movie/now_playing"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener las películas que están echando en cines"}

#las que están echando en la tele
def top_rated():
    url = f"{BASE_URL}/movie/top_rated"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener las películas mejor calificadas"}

#detalles peliculas
def detalle_pelicula(pelicula_id):
    url = f"{BASE_URL}/movie/{pelicula_id}"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener los detalles de la película"}