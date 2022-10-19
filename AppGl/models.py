from django.db import models

class Receta(models.Model):
    imagen = models.ImageField(upload_to = "recetas", null=True)
    nombre = models.CharField(max_length=100)
    ingredientes = models.CharField(max_length=240)
    tiempo = models.IntegerField()
    preparacion = models.TextField(max_length=2000)

class ImRecetas(models.Model):
    pass
