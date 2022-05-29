from django.db import models

class Directors(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del director")
    lastname = models.CharField(max_length=64, help_text="Apellido del director")


    def __str__(self):
        return self.name

class Films(models.Model):
    title = models.CharField(max_length=64, help_text="Nombre de la pelicula")
    description = models.TextField(max_length=500, help_text="Descripcion")
    year = models.IntegerField()
    director = models.ForeignKey('Directors', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
