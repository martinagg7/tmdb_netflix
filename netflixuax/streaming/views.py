from django.shortcuts import render
from .scripts.peliculas import peliculas_populares,now_playing,top_rated,detalle_pelicula

#para la página incio peliculas populares
def inicio(request):
    peliculas = peliculas_populares()  
    return render(request, 'streaming/inicio.html', {'peliculas': peliculas})

def now_playing_view(request):
    peliculas = now_playing()
    return render(request, 'streaming/now_playing.html', {'peliculas': peliculas})

def top_rated_view(request):
    peliculas = top_rated()
    return render(request, 'streaming/top_rated.html', {'peliculas': peliculas})

def detalle(request, pelicula_id):
    detalles = detalle_pelicula(pelicula_id)
    return render(request, 'streaming/detalle.html', {'detalles': detalles})