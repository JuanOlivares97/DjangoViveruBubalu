from django.db import models
from django.forms import BooleanField

# Create your models here.

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nom_producto = models.CharField(max_length=40)
    stock = models.IntegerField()
    precio = models.IntegerField()
    img_producto = models.CharField(max_length=1000, null=True)

    def __str__(self) -> str:
        return self.nom_producto

class Promocion(models.Model):
    id_promocion = models.IntegerField(primary_key=True)
    nom_promocion = models.CharField(max_length=40)
    porcentaje = models.IntegerField()
    fecha_ini = models.DateTimeField()
    fecha_termino =models.DateTimeField()

    def __str__(self) -> str:
        return self.nom_promocion

class nuevoUsuario(models.Model):
    nombre=models.CharField(max_length=150)
    apellidos=models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    pwd = models.CharField(max_length=150)
    suscrito = models.BooleanField(null=False, default=False)

    def __str__(self) -> str:
        return self.nombre
    













class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.nombreCategoria

class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=6)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.marca+" "+self.patente

    

