from django.db import models
from .listas import LISTA_PAISES,TIPO_SEXO, TIPO_MASCOTA, SUBTIPO_MASCOTA
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Persona(models.Model):
    rut=models.CharField(max_length=10, primary_key=True, null=False)
    nombre=models.CharField(max_length=50, null=False)
    apellido=models.CharField(max_length=50, null=False)
    f_nacto=models.DateField()
    sexo=models.CharField(max_length=1, default='O', choices=TIPO_SEXO)
    pais=models.CharField(max_length=20, choices=LISTA_PAISES, default='CL')

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