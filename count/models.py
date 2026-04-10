from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name='Nome Completo')
    job_title = models.CharField(max_length=255, verbose_name='Cargo')
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, verbose_name='Foto de Perfil')
