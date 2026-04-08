from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Conteudo")
    author = models.CharField(max_length=100, verbose_name="Autor" )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d',blank=True)
    image_alt = models.CharField(max_length=250, verbose_name="descrição da imagem")
    image_caption = models.CharField(max_length=250, blank=True, verbose_name="legenda da imagem")
