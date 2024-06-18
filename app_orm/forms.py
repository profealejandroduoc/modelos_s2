from django import forms
from .models import Persona, User
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    pass

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','direccion','telefono','password1','password2']


class PersonaForm(forms.ModelForm):
    
    rut=forms.CharField(max_length=100, help_text="Rut sin puntos con guión")
    f_nacto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

    
    class Meta:
        model = Persona
        fields = ['rut','nombre','apellido','foto','f_nacto','sexo','pais']


class UpdPersonaForm(forms.ModelForm):
    
 
    f_nacto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

    
    class Meta:
        model = Persona
        fields = ['nombre','apellido','foto','f_nacto','sexo','pais']

