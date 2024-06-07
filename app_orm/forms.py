from django import forms
from .models import Persona


class PersonaForm(forms.ModelForm):
    
    rut=forms.CharField(max_length=100, help_text="Rut sin puntos con guión")
    f_nacto=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    

    
    class Meta:
        model = Persona
        fields = ['rut','nombre','apellido','foto','f_nacto','sexo','pais']

