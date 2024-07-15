import datetime
from django.db import models
from distutils.command.upload import upload
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

class Categoria1(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id Categoria') 
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria2(models.Model):
    idCiudad = models.IntegerField(primary_key=True, verbose_name='Id Ciudad') 
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.ciudad

class Vehiculo(models.Model):
    placa = models.CharField(primary_key=True, max_length=6, verbose_name='Id Vehiculo')
    marca = models.CharField(max_length=50, verbose_name='Marca')
    modelo = models.CharField(max_length=50,verbose_name='Modelo')
    capacidad = models.PositiveIntegerField(verbose_name='Capacidad')  # Capacidad en kg o número de pasajeros
    precio=models.IntegerField(blank=True, null=True, verbose_name="Precio")
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')
    categoria1= models.ForeignKey('Categoria1', on_delete=models.CASCADE, verbose_name='Categoria1')
    categoria2= models.ForeignKey('Categoria2', on_delete=models.CASCADE, verbose_name='Categoria2')
    

    def __str__(self):
        return self.placa
    

class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
  
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Vehiculo', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)