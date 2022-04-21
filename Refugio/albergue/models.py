from cProfile import label
from turtle import update
from venv import create
from django.db import models
from multiselectfield import MultiSelectField
from numpy import mask_indices

# Create your models here.


class CategoriaMascota(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="CategoriaMascota"
        verbose_name_plural="CategoriasMascota"
    
    def __str__(self):
        return self.nombre


class Vacuna(models.Model):
    vacuna=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Vacuna"
        verbose_name_plural="Vacunas"
    
    def __str__(self):
        return self.vacuna
    
class Sexo(models.Model):
    sexo=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.sexo
        

vacuna_lib=(
    ("parvovirus", "Parvovirus"),
    ("moquillo", "Moquillo"),
    ("hepatitis", "Hepatitis"),
    ("adenovirus","Adenovirus"),
    ("rabia", "Rabia"),
    ("herpesvirus","Herpesvirus"),
    ("calicivirus","Calicivirus")
)


class Mascota(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaMascota, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="albergue", null=True, blank=True)
    disponibilidad=models.BooleanField(default=True)
    alimentacion=models.CharField(max_length=50,null=True, blank=True)
    vacunas=MultiSelectField(choices=vacuna_lib)
    raza=models.CharField(max_length=40)
    sexo_mascota=models.ForeignKey(Sexo, on_delete=models.CASCADE, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name="Mascota"
        verbose_name_plural="Mascotas"
        


class Adopcion(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=8)
    direccion=models.CharField(max_length=60)
    email=models.EmailField()
    nombre_mascota=models.CharField(max_length=40)
    estado=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Adopcion"
        verbose_name_plural="Adopciones"
