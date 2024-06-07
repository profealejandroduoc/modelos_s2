from django.shortcuts import render
from datetime import datetime, date
from .models import Persona
from django.shortcuts import get_object_or_404,redirect
from .forms import PersonaForm
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


def crearpersona(request):
    miformulario=PersonaForm()



    if request.method=="POST":
        miformulario=PersonaForm(data=request.POST,files=request.FILES)
        if miformulario.is_valid():

            miformulario.save()
            return redirect(to='personas')

    datos={
        "form":miformulario
    }



    return render(request,'app_orm/crearpersona.html',datos)

def detallepersona(request,id):
    persona=get_object_or_404(Persona,rut=id)
    #persona=Persona.objects.get(rut=id) #None
    #print(persona)
    datos={

        "persona":persona
    }

    return render(request,'app_orm/detallepersona.html', datos)