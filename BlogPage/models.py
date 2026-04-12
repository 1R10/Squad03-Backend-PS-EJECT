from django.db import models
from count.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Conteudo")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d',)
    image_alt = models.CharField(max_length=250, verbose_name="descrição da imagem", blank=True)
    image_caption = models.CharField(max_length=250, verbose_name="legenda da imagem")
