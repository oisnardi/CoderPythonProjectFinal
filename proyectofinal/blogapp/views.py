from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Page

from blogapp.forms import (
    UserRegistrationForm,
    UserEditForm,
    AvatarFormulario,
)


def index(request):
    pages = Page.objects.all()
    return render(request, 'index.html', {'pages': pages})

def about(request):
    return render(request, 'about.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Reemplaza 'home' con la URL a la que quieres redirigir después del login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

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
                return redirect('index')  # Redirigir a la página de registro exitoso
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

                return render(request, 'index.html', {"mensaje": f"Bienvenido {username}"})                
            else:
                return render(request, 'index.html', {"mensaje": f"Usuario o contraseña invalidos"})

        else:
            return render(request, "index.html", {"mensaje": "Datos form incorrectos"})

    form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# END SECCIÓN USUARIOS
