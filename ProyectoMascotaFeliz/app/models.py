from multiprocessing.sharedctypes import Value
from optparse import Values
from sys import maxsize
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Cliente (models.Model):
    idCliente = models.CharField(primary_key=True, max_length=50, verbose_name="IdCliente")
    nombreCliente = models.CharField(max_length=50, verbose_name="NombreCliente")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    comuna = models.CharField(max_length=50, verbose_name="Comuna")
    correo = models.EmailField(verbose_name="Correo", default="example@gmail.com")
    telefono = models.PositiveIntegerField(verbose_name="Telefono")
    direccion = models.CharField(max_length=50, verbose_name="Direccion")
 
    def __str__(self):
        return self.idCliente

class Producto (models.Model):
    idProducto = models.CharField(primary_key=True, max_length=9, verbose_name="IdProducto")
    nombreProducto = models.CharField(max_length=50, verbose_name="NombreProducto")
    descripcion = models.TextField(max_length=100, verbose_name="Descripcion" )
    precioProducto = models.PositiveIntegerField(verbose_name="PrecioProducto", default= "0000")
    stockProducto = models.PositiveIntegerField(verbose_name="StockProducto", default= "0000")



    imagen = models.ImageField(upload_to="imagenes", null=True)



    def __str__(self):
        return self.idProducto


def create_profile(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance)


post_save.connect(create_profile, sender=Cliente)