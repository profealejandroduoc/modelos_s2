from django.shortcuts import render
from datetime import datetime, date
from .models import Persona
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    hoy=datetime.now()
    texto="Este es un texto desde la vista index"
    asistentes=6
    lista=[1,2,3,4,5,7]

    datos={
        "fecha":hoy,
        "texto":texto,
        "asistentes":asistentes,
        "lista":lista
    }


    return render(request,'app_orm/index.html', datos)

def personas(request):
    personas=Persona.objects.all()

    datos={
        "personas":personas
    }

    return render(request,'app_orm/personas.html',datos)

def detallepersona(request,id):
    persona=get_object_or_404(Persona,rut=id)
    #print(persona)
    datos={

        "persona":persona
    }

    return render(request,'app_orm/detallepersona.html', datos)