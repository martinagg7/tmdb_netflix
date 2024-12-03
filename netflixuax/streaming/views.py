from django.shortcuts import render
from .scripts.peliculas import peliculas_populares, now_playing, top_rated, detalle_pelicula
from .scripts.series import obtener_series_populares,obtener_detalle_serie,obtener_airing_today
from .scripts.search import obtener_buscar
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

def detalle_serie(request, serie_id):
    serie_detalles = obtener_detalle_serie(serie_id)  
    return render(request, 'streaming/series/detalle_serie.html', {'detalles': serie_detalles})

def airing_today(request):
    series = obtener_airing_today()  
    return render(request, 'streaming/series/airing_today.html', {'series': series})

#BUSQUEDA


def buscar(request):
    texto = request.GET.get('q', '')  # Obtiene el texto ingresado en el formulario
    resultados = {}

    if texto:  # Si hay texto en la búsqueda
        resultados = obtener_buscar(texto)

    return render(request, 'streaming/buscar.html', {'resultados': resultados, 'texto': texto})