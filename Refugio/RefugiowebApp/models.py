from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class Datos(models.Model):
    Nombre=models.CharField(max_length=50)
    Telefono=models.CharField(max_length=8)
    Direccion=models.CharField(max_length=50,blank=True, null=True)
    Mascota=models.CharField(max_length=40,blank=True, null=True)
    Ocupacion=models.CharField(max_length=50,blank=True, null=True)
    Edad_de_mascota=models.CharField(max_length=20,blank=True, null=True)
    Foto=models.ImageField(upload_to='datos', blank=True, null=True)
    Fecha=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)



    def __str__ (self):
        return self.Nombre
