# scripts/series.py
import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"

# Función para obtener las Series Populares
def series_populares():
    url = f"{BASE_URL}/tv/popular"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudieron obtener las series populares"}