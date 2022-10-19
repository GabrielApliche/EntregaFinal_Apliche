from django import forms
from AppGl.models import Receta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecetaFormulario(forms.Form):
    imagen = forms.ImageField()
    nombre = forms.CharField(max_length=72)
    ingredientes = forms.CharField(max_length=240)
    tiempo = forms.IntegerField()
    preparacion = forms.CharField(widget=forms.Textarea)

class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "password1", "password2"] 
        help_texts = {
            "username" : None,
        }

class EditarReceta(forms.ModelForm):

    class Meta:

        model = Receta
        fields = ["imagen", "nombre", "ingredientes", "tiempo", "preparacion"]
