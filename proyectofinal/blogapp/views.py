from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Avatar, Page

from blogapp.forms import (
    AvatarFormulario,
    PageForm,
    UserRegistrationForm,
    UserEditForm,
)

def about(request):
    return render(request, 'about.html')

## SECCIÓN PAGINAS CRUD
def index(request):
    pages = Page.objects.all()
    return render(request, 'index.html', {'pages': pages})

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page_detail.html', {'page': page})

@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.owner = request.user
            page.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'page_form.html', {'form': form})

@login_required
def page_update(request, pk):
    page = get_object_or_404(Page, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = PageForm(instance=page)
    return render(request, 'page_form.html', {'form': form})

@login_required
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk, owner=request.user)
    if request.method == 'POST':
        page.delete()
        return redirect('page_list')
    return render(request, 'page_confirm_delete.html', {'page': page})
## END CRUD
    
# SECCIÓN USUARIOS
def registrar(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Autenticar al usuario después del registro
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Set URL Avatar to Sessión
                avatar = Avatar.objects.get_or_create(user=user)[0]

                if avatar.image:
                    request.session['avatar_url'] = avatar.image.url
    
                return redirect('index')
        else:
            messages.error(request, 'Datos incorrectos')
       
    else:
        form = UserRegistrationForm()

    return render(request, 'usuario_registrar.html', {'form': form})

def login_request(request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                avatar = Avatar.objects.get_or_create(user=user)[0]

                # Set URL Avatar to Sessión
                avatar = Avatar.objects.get_or_create(user=user)[0]

                if avatar.image:
                    request.session['avatar_url'] = avatar.image.url
    
                return redirect('index')
            else:
                messages.error(request, 'Datos incorrectos')
        else:
            messages.error(request, 'Datos incorrectos')
            
    form = AuthenticationForm()

    return render(request, "usuario_login.html", {"form": form})

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        print(f"editar_perfil -- POST")
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            print(f"email: {informacion.get("email")}")
            usuario.email = informacion.get("email")
            print(f"last_name: {informacion.get("last_name")}")
            usuario.last_name = informacion.get("last_name")
            print(f"first_name: {informacion.get("first_name")}")
            usuario.first_name = informacion.get("first_name")

            print(f"password1: {informacion.get("password1")}")

            usuario.save()

            return redirect('index')


    print(f"editar_perfil -- GET")
    formulario = UserEditForm(initial={"first_name": usuario.first_name,
                                       "last_name": usuario.last_name,
                                        "email": usuario.email,})
    
    # Se quitan las Passwords para que no se cambien
    #formulario.fields.pop('password1', None)
    #formulario.fields.pop('password2', None)

    return render(request, "usuario_editar.html", {"form": formulario}) 

@login_required
def avatar(request):
    if request.method == "POST":
        print("avatar - POST")
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            print("avatar - Is_Valid!")
            user = request.user

            avatar = Avatar.objects.filter(user=user).first()
            if avatar:
                avatar.delete()

            avatar = Avatar.objects.create(user=user, image=formulario.cleaned_data.get("image"))

            print("avatar - Success!")
            #messages.success(request, 'Imagen de perfil actualizada exitosamente.')

            # Set URL Avatar to Sessión
            avatar = Avatar.objects.get_or_create(user=user)[0]

            if avatar.image:
                request.session['avatar_url'] = avatar.image.url
  
            return redirect('index')


    formulario = AvatarFormulario()

    return render(request, 'usuario_avatar.html', {"form": formulario})
# END SECCIÓN USUARIOS
