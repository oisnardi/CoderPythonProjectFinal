from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Page

from blogapp.forms import (
    UserRegistrationForm,
    UserEditForm,
)


def index(request):
    pages = Page.objects.all()
    return render(request, 'index.html', {'pages': pages})

def about(request):
    return render(request, 'about.html')

## SECCIÓN PAGINAS CRUD
@login_required
class PageCreateView(CreateView):
    model = Page
    template_name = 'page_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('page_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

@login_required
class PageUpdateView(UpdateView):
    model = Page
    template_name = 'page_form.html'
    fields = ['title', 'content', 'image']
    success_url = reverse_lazy('page_list')

@login_required
class PageDeleteView(DeleteView):
    model = Page
    template_name = 'page_confirm_delete.html'
    success_url = reverse_lazy('page_list')

def page_detail(request, pk):
    page = Page.objects.get(pk=pk)
    return render(request, 'page_detail.html', {'page': page})
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
                messages.success(request, '¡Usuario registrado exitosamente!')

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

                return render(request, 'index.html')                
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

            return render(request, "index.html")


    print(f"editar_perfil -- GET")
    formulario = UserEditForm(initial={"first_name": usuario.first_name,
                                       "last_name": usuario.last_name,
                                        "email": usuario.email,})
    
    # Se quitan las Passwords para que no se cambien
    #formulario.fields.pop('password1', None)
    #formulario.fields.pop('password2', None)

    return render(request, "usuario_editar.html", {"form": formulario}) 

# END SECCIÓN USUARIOS
