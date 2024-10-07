from django.db import models
from django.core.validators import FileExtensionValidator

class Musica(models.Model):
    titulo=models.CharField(max_length=100)
    artista=models.CharField(max_length=100)
    album=models.CharField(max_length=100, blank=True)
    capa=models.ImageField(upload_to='capas/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def _str_ (self):
        return f"{self.titulo} {self.artista}"
    
class Playlist(models.Model):
    nome= models.CharField(max_length=100)
    musicas= models.ManyToManyField(Musica)

    def __str__(self):
        return self.nome
