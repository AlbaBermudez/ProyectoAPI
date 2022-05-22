from tabnanny import verbose
from django.db import models

# Create your models here.

class articulo(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.FloatField()
    descripcion=models.CharField(max_length=200)
    
    class Meta:
        verbose_name='articulo'
        verbose_name_plural='articulos'
    
    def __str__(self):
        return self.nombre

