from tkinter import CASCADE
from django.db import models

# Create your models here.

class Categoria(models.Model):
    category=models.CharField(max_length=20)
    def __str__(self):
        return self.category


class Producto(models.Model):
   
    codigo = models.CharField(max_length=18)
    nombre= models.CharField(max_length=65)
    descripcion=models.TextField()
    stock = models.IntegerField()
    puni=models.DecimalField(max_digits=6, decimal_places=2)
    pkilo=models.DecimalField(max_digits=6, decimal_places=2)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.CharField(max_length=500, null=True, blank=True)
    
    


    def __str__(self):
        return self.nombre

