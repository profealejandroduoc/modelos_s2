from django.contrib import admin
from .models import Persona, Mascota, User




class AdmPersona(admin.ModelAdmin):
    list_display=['rut','nombre','apellido','foto','f_nacto','sexo','pais']
    list_filter=['apellido','f_nacto','sexo']
    #list_editable=['nombre','apellido','f_nacto', 'sexo','pais']


class AdmMascota(admin.ModelAdmin):
    list_display=['id','nombre', 'tipo','edad', 'subtipo', 'propietario']
    list_editable=['nombre', 'tipo','edad', 'subtipo', 'propietario']
    list_filter=['propietario']


class AdmUser(admin.ModelAdmin):
    filter_horizontal = ('groups','user_permissions') 


# Register your models here.
admin.site.register(Persona, AdmPersona)
admin.site.register(Mascota, AdmMascota)
admin.site.register(User, AdmUser)