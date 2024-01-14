from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Sección: Usuarios
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Requerido. Máximo 30 caracteres. Solo letras, números y @/./+/-/_ permitidos.')
    email = forms.EmailField(label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        max_length=254,
        required=True,
        help_text='Requerido. Debe ser una dirección de correo electrónico válida.')
    password1 = forms.CharField(label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        help_text='Requerido. Al menos 8 caracteres. No puede ser solo numérico.')
    password2 = forms.CharField(label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
        help_text='Requerido. Ingrese la misma contraseña que antes para verificación.')
    last_name = forms.CharField(label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Requerido. Máximo 30 caracteres.')
    first_name = forms.CharField(label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=30,
        required=True,
        help_text='Requerido. Máximo 30 caracteres.')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserEditForm(forms.Form):
    email = forms.EmailField(label="Ingesar email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User 
        fields = [ "email", "password1", "password2", "last_name", "first_name"]

class AvatarFormulario(forms.Form):
    image = forms.ImageField()

    

# End Sección Usuarios

