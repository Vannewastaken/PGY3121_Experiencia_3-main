from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from .models import Categoria1,Categoria2,Vehiculo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegistroUserForm(UserCreationForm):
    first_name = forms.CharField(min_length=3, max_length=10, required=True)
    last_name = forms.CharField(min_length=3, max_length=15, required=True)
    email = forms.EmailField(max_length=50, help_text='Por favor ingrese una dirección de correo válida.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email de usuario ya está en uso.")
        return email   

class UserUpdateForm(forms.ModelForm):
    password = None  # Excluir los campos de contraseña
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': forms.HiddenInput()
        } 
class CamionForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['placa', 'marca', 'modelo', 'capacidad','precio','imagen','categoria1','categoria2','stock']
        labels={
            'placa': 'Id Camión',
            'marca':'Marca',
            'modelo': 'Modelo',
            'capacidad': 'Capacidad',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'categoria1': 'Categoria1',
            'categoria2': 'Categoria2',
            'stock':'Stock'
        }
        widgets={
            'placa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la patente del camión',
                    'id': 'placa'
                }
            ),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la marca del camión',
                    'id': 'marca'
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el modelo del camión',
                    'id': 'modelo'
                }
            ),
            'capacidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese la capacidad del camión',
                    'id': 'capacidad'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el valor del camión',
                    'id': 'precio'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'categoria1': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria1'
                }
            ),
            
            'categoria2': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria2'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese el stock de este camión',
                    'id': 'stock'
                }
            ),
        }
    def clean_placa(self):
        placa = self.cleaned_data['placa']
        if self.instance and self.instance.pk:
            if Vehiculo.objects.filter(placa=placa).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Ya existe un vehículo con esta placa.")
        else:
            if Vehiculo.objects.filter(placa=placa).exists():
                raise forms.ValidationError("Ya existe un vehículo con esta placa.")
        return placa

    def clean_capacidad(self):
        capacidad = self.cleaned_data.get('capacidad')
        if capacidad <= 0:
            raise ValidationError("La capacidad debe ser un número positivo.")
        return capacidad

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise ValidationError("El precio debe ser un número positivo.")
        return precio