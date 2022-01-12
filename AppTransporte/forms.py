from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields


class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasenia', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class PasajeroFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    numeroDeDocumento = forms.IntegerField()
    vacunado = forms.BooleanField()

class ChoferFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    numeroDeDocumento = forms.IntegerField()
    numeroDeLicencia = forms.IntegerField()

class TransporteFormulario(forms.Form):
    tipo = forms.CharField() #Tipo: Aereo o terrestre
    empresa = forms.CharField() #Empresa a cargo
    capacidad = forms.IntegerField() #Capacidad del transporte
    patente = forms.IntegerField()

class TerminalFormulario(forms.Form):
    nombre = forms.CharField()
    ubicacion = forms.CharField()