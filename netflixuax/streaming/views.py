from django.shortcuts import render
from .scripts.peliculas import obtener_peliculas_populares

def inicio(request):
    peliculas = obtener_peliculas_populares()  # Llama a la función para obtener las películas populares
    return render(request, 'streaming/inicio.html', {'peliculas': peliculas})