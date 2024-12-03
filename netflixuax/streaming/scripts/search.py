import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"

def obtener_buscar(texto): # texto es lo que introduce usuario
   
    url = f"{BASE_URL}/search/multi"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
        "query": texto,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se encontraron resultados"}