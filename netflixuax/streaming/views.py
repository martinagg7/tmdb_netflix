from django.shortcuts import render
from .scripts.peliculas import peliculas_populares

#para la página incio peliculas populares
def inicio(request):
    peliculas = peliculas_populares()  
    return render(request, 'streaming/inicio.html', {'peliculas': peliculas})