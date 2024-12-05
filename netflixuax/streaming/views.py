from django.shortcuts import render,redirect
from .scripts.peliculas import peliculas_populares, now_playing, top_rated, detalle_pelicula
from .scripts.series import obtener_series_populares,obtener_detalle_serie,obtener_airing_today
from .scripts.search import obtener_buscar
#para peliculas favoritas
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FavoriteMovie

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
    texto = request.GET.get('q', '') #cogemos lo que el usuario pone en la barra de busqueda
    resultados = {}

    if texto: 
        resultados = obtener_buscar(texto)

    return render(request, 'streaming/buscar.html', {'resultados': resultados, 'texto': texto})

#PELICULAS FAVORITAS

"""add_to_favorites:nos permite crear una instancia de favorite movie asociada a un usario solo si este está verificado"""
@login_required 
def add_to_favorites(request, movie_id):
    title = request.GET.get("title")
    poster_path = f"https://image.tmdb.org/t/p/w500{request.GET.get('poster_path')}"
    

    if FavoriteMovie.objects.filter(user=request.user, movie_id=movie_id).exists():
        messages.info(request, f"{title} ya está en  favoritos.")
    else:
        FavoriteMovie.objects.create(
            user=request.user,
            movie_id=movie_id,
            title=title,
            poster_path=poster_path
        )
        messages.success(request, f"{title} añadida a tus favoritos.")
    return redirect('favoritos')

""""favoritos:nos lleva al template donde se muestran las pelis faoviritas del usuario"""
@login_required
def favoritos(request):
    favoritos = FavoriteMovie.objects.filter(user=request.user)
    return render(request, 'streaming/favoritos.html', {'favoritos': favoritos})