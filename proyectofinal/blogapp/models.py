from django.db import models
from django.contrib.auth.models import User

# Sección Paginas
class Page(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='pages')
    published_date = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# End --> Sección Paginas


# Sección Usuarios
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    # Agrega campos adicionales si es necesario para tu aplicación

    def __str__(self):
        return self.user.username

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

# End --> Sección Usuarios