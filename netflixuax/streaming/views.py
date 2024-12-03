from django.shortcuts import render
from .scripts.peliculas import buscar_peliculas


def buscar(request):
    query = request.GET.get('q', '')
    resultados = buscar_peliculas(query) if query else {}
    return render(request, 'streaming/buscar.html', {'resultados': resultados, 'query': query})