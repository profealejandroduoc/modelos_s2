from django.db import models
from .listas import LISTA_PAISES,TIPO_SEXO, TIPO_MASCOTA, SUBTIPO_MASCOTA
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    direccion=models.CharField('Dirección',max_length=500,null=True)
    telefono=models.CharField('Teléfono',max_length=9, null=True)



# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10, primary_key=True, null=False)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    foto=models.ImageField("Imagen",upload_to='personas',null=True)
    f_nacto=models.DateField("Fecha de Nacimiento")
    sexo=models.CharField(max_length=10, default='Otro', choices=TIPO_SEXO)
    pais=models.CharField(max_length=50, choices=LISTA_PAISES, default='CL')

    def __str__(self):
        return f"RUT: {self.rut} NOMBRE: {self.nombre} {self.apellido}"
    
class Mascota(models.Model):
    nombre=models.CharField(max_length=25, null=False)
    tipo=models.CharField(max_length=30, choices=TIPO_MASCOTA)
    edad=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(300)])
    subtipo=models.CharField(max_length=20, choices=SUBTIPO_MASCOTA, default='Sin subtipo')
    propietario=models.ForeignKey(Persona, on_delete=models.PROTECT)


    def __str__(self):
        return self.nombre