from django.db import models
from django.contrib.auth.models import User



"""
FavoriteMovie:sirve para guardar las peliculas favoritas de cada usuario
Conectamos las peliculas del usuario con este a través de ForeignKey, de tal manera
    1.Un usario puede tener varias pelis favoritas
    2.Cada peli esta asociada a un usuario , si se elimina el usuario se eliminan las pelis asociadas a este

"""
class FavoriteMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_movies')
    movie_id = models.IntegerField()  
    title = models.CharField(max_length=200)
    poster_path = models.URLField(blank=True, null=True)  

    def __str__(self):
        return f"{self.title} - {self.user.username}"