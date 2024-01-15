from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import avatar, editar_perfil, index, login_request, page_create, page_delete, page_detail, about, page_list, page_update, registrar

urlpatterns = [
    # Rutas para el administrador de Django
    path('admin/', admin.site.urls),

    # Rutas para el blog
    path('', index, name='index'),
    # Usuario
    path('login/', login_request, name='login'),
    path('registrar/', registrar, name='registrar'),
    path("logout", LogoutView.as_view(template_name="usuario_logout.html"), name='Logout'),
    path('perfil/', editar_perfil, name='editar_perfil'),
    path('avatar', avatar, name='avatar'),
    # Pages
    path('pages/', page_list, name='page_list'),
    path('pages/<int:pk>/', page_detail, name='page_detail'),
    path('pages/new/', page_create, name='page_create'),
    path('pages/<int:pk>/edit/', page_update, name='page_update'),
    path('pages/<int:pk>/delete/', page_delete, name='page_delete'),
    # Acerca de
    path('about/', about, name='about'),
]