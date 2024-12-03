from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('now_playing/', views.now_playing_view, name='now_playing'),
    path('top_rated/', views.top_rated_view, name='top_rated'),
    path('detalle/<int:pelicula_id>/', views.detalle, name='detalle')
]