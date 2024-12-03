def buscar_series(query):
    url = f"{BASE_URL}/search/tv"
    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": query,
        "language": "es-ES",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return {"error": "No se pudo conectar a TMDb"}