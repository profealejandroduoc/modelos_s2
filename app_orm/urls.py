from django.urls import path
from .views import index, personas, detallepersona,crearpersona,modificar, eliminar,salir

urlpatterns = [
    path('', index, name='index'),
    path('personas/',personas,name='personas'),
    path('detallepersona/<id>',detallepersona,name='detallepersona'),
    path('crearpersona/',crearpersona,name='crearpersona'),
    path('modificar/<id>',modificar,name="modificar"),
    path('eliminar/<id>',eliminar, name="eliminar"),
    path('salir/',salir,name='salir')

]
