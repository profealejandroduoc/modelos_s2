from django.urls import path
from .views import index, personas, detallepersona,crearpersona

urlpatterns = [
    path('', index, name='index'),
    path('personas/',personas,name='personas'),
    path('detallepersona/<id>',detallepersona,name='detallepersona'),
    path('crearpersona/',crearpersona,name='crearpersona')
]
