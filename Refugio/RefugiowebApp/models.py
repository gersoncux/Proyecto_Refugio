from tabnanny import verbose
from django.db import models

# Create your models here.

class Registro(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha=models.DateTimeField(auto_now_add=True)
    raza=models.CharField(max_length=50)
    alimento=models.CharField(max_length=50)
    enfermedad=models.BooleanField()
    vacunas=models.BooleanField()
    foto=models.ImageField()

    class Meta:
        verbose_name='registro'
        verbose_name_plural='registros'
    def __str__(self):
        return self.titulo

