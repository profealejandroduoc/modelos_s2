from django.contrib import admin
from .models import Persona, Mascota

class AdmPersona(admin.ModelAdmin):
    list_display=['rut','nombre','apellido','f_nacto','sexo','pais']
    list_filter=['apellido','f_nacto','sexo']
    list_editable=['nombre','apellido','f_nacto', 'sexo','pais']


class AdmMascota(admin.ModelAdmin):
    list_display=['id','nombre', 'tipo','edad', 'subtipo', 'propietario']
    list_editable=['nombre', 'tipo','edad', 'subtipo', 'propietario']
    list_filter=['propietario']

# Register your models here.
admin.site.register(Persona, AdmPersona)
admin.site.register(Mascota, AdmMascota)