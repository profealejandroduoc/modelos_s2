from django.shortcuts import render
from datetime import datetime, date
from .models import Persona, User
from django.shortcuts import get_object_or_404,redirect
from .forms import PersonaForm, UpdPersonaForm, UserForm
from os import remove, path
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
# Create your views here.


def crearcuenta(request):
    form=UserForm()

    datos={
        'form':form
    }

    if request.method=="POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            usr=form.cleaned_data["username"]
            
            usuario = User.objects.get(username=usr)
            permiso = Permission.objects.get(codename='add_persona') #import Permission 
            usuario.user_permissions.add(permiso)

            messages.success(request,"Nuevo usuario registrado")
            return redirect(to="login")
        
    return render(request,'registration/crearcuenta.html', datos)

def salir(request):
    logout(request)
    messages.info(request,'Sesión Cerrada')
    return redirect(to="index")

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
    usuario=request.user
    print("PERMISOS********",usuario.get_all_permissions())
    agregar=usuario.has_perm('app_orm.add_persona')
    print(agregar)
    datos={
        "personas":personas,
        "agregar":agregar
    }

    return render(request,'app_orm/personas.html',datos)

@login_required
@permission_required('app_orm.add_persona') 
def crearpersona(request):
    miformulario=PersonaForm()

    if request.method=="POST":
        miformulario=PersonaForm(data=request.POST,files=request.FILES)
        if miformulario.is_valid():
            miformulario.save()
            #from django.contrib import messages
            messages.success(request, "Persona agregada con éxito")
            
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

@login_required
@permission_required('app_orm.change_persona') 
def modificar(request,id):
    persona=get_object_or_404(Persona,rut=id)
    form=UpdPersonaForm(instance=persona)
   
    datos={
        "form":form,
        "persona":persona
  
    }

    if request.method=="POST":
        form=UpdPersonaForm(data=request.POST,files=request.FILES, instance=persona)
        if form.is_valid():

            form.save()
            
            messages.warning(request,'Persona modificada')
            return redirect(to='personas')

    return render(request,'app_orm/modificar.html', datos)

@login_required
@permission_required('app_orm.delete_persona') 
def eliminar(request,id):
    persona=get_object_or_404(Persona,rut=id)
    datos={
        "persona":persona
    }

    if request.method=="POST":
        #from os import remove, path
        #from django.conf import settings
        remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+str(persona.foto.url).replace('/','\\')))
        persona.delete()       
        return redirect(to="personas")
    return render(request,'app_orm/eliminar.html', datos)