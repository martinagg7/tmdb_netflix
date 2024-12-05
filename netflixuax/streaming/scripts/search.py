import requests
from django.conf import settings

BASE_URL = "https://api.themoviedb.org/3"

#para buscar tanto en series como en pelis por nombre
def obtener_buscar(texto): 
   
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