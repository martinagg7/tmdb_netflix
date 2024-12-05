import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"

# para buscar series populares
def obtener_series_populares():
    url = f"{BASE_URL}/tv/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener las series populares"}

#cuando  hace click en una peli salgan detalles
def obtener_detalle_serie(serie_id):
    url = f"{BASE_URL}/tv/{serie_id}"
    params = {
        "api_key": settings.TMDB_API_KEY,  
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener los detalles de la serie"}

#las que están echando
def obtener_airing_today():
    url = f"{BASE_URL}/tv/airing_today"  
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener las series que se emiten hoy"}