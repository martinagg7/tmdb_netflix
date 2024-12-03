from django.shortcuts import render
from .scripts.peliculas import peliculas_populares, now_playing, top_rated, detalle_pelicula
from .scripts.series import obtener_series_populares

def inicio(request):
    peliculas = peliculas_populares()
    return render(request, 'streaming/peliculas/now_playing.html', {'peliculas': peliculas})

# PARA PELICULAS
def now_playing_view(request):
    peliculas = now_playing()
    return render(request, 'streaming/peliculas/now_playing.html', {'peliculas': peliculas})

def top_rated_view(request):
    peliculas = top_rated()
    return render(request, 'streaming/peliculas/top_rated.html', {'peliculas': peliculas})

def detalle(request, pelicula_id):
    detalles = detalle_pelicula(pelicula_id)
    return render(request, 'streaming/peliculas/detalle.html', {'detalles': detalles})

#PARA SERIES
def series_populares(request):
    series = obtener_series_populares() 
    return render(request, 'streaming/series/series_populares.html', {'series': series})