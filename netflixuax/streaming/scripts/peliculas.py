import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"

def buscar_peliculas(query):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": query,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudo conectar a TMDb"}