from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=20, verbose_name="Title")
    content = models.TextField(verbose_name="Conteudo")
    author = models.CharField(max_length=100, verbose_name="Autor" )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    image = models.ImageField(upload_to='blog_images/',blank=True)
    image_caption = models.CharField(max_length=250, blank=True)

