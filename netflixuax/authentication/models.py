from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritos')
    tipo = models.CharField(max_length=10, choices=[('pelicula', 'Película'), ('serie', 'Serie')])
    titulo = models.CharField(max_length=200)
    tmdb_id = models.IntegerField()
    poster_path = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo.capitalize()}: {self.titulo}"