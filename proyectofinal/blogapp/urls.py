from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import PageCreateView, PageDeleteView, PageUpdateView, avatar, editar_perfil, index, login_request, page_detail, about, registrar

urlpatterns = [
    # Rutas para el administrador de Django
    path('admin/', admin.site.urls),

    # Rutas para el blog
    path('', index, name='index'),
    # Usuario
    path('login/', login_request, name='login'),
    path('registrar/', registrar, name='registrar'),
    path("logout", LogoutView.as_view(template_name="index.html"), name='Logout'),
    path('perfil/', editar_perfil, name='editar_perfil'),
    path('avatar', avatar, name='avatar'),
    # Page
    # path('create/', PageCreateView.as_view(), name='page_create'),
    # path('<int:pk>/update/', PageUpdateView.as_view(), name='page_update'),
    # path('<int:pk>/delete/', PageDeleteView.as_view(), name='page_delete'),
    # path('pages/<int:pk>', page_detail, name='page_detail'),
    # Acerca de
    path('about/', about, name='about'),
]