from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('pelicula/now-playing/', views.now_playing_view, name='now_playing'),
    path('pelicula/top-rated/', views.top_rated_view, name='top_rated'),
    path('pelicula/detalle/<int:pelicula_id>/', views.detalle, name='detalle'),
    path('series/populares/', views.series_populares, name='popular_series'),
    path('series/detalle/<int:serie_id>/', views.detalle_serie, name='detalle_serie'),
    path('series/airing_today/', views.airing_today, name='airing_today_series'),
    path('buscar/', views.buscar, name='buscar'),
     
    
    
]