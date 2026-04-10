# Squad03-Backend-PS-EJECT
Repositório destinado á equipe de Back-End do Squad03 no processo seletivo da EJECT 2026.1

## Venv

O arquivo [requirements.txt](requirements.txt) tem as frameworks e bibliotecas a serem usadas no projeto.

Comado a ser usado para instalar os requerimentos:

```
pip install -r requirements.txt
```

## Diagrama de Classe
``` mermaid
classDiagram

class AbstractUser

class User {
  +full_name: CharField(255)
  +job_title: CharField(255)
  +image: ImageField(upload_to='profile_images/', null=True, blank=True)
}

class BlogPost {
  +title: CharField(150)
  +content: TextField
  +author: ForeignKey(User)
  +created_at: DateTimeField(auto_now_add=True)
  +image: ImageField(upload_to='blog_images/%Y/%m/%d')
  +image_alt: CharField(250, blank=True)
  +image_caption: CharField(250)
}

class Hospedes {
  +nome: CharField(200)
  +email: EmailField(200)
  +celular: TextField
  +adulto: PositiveIntegerField(default=1)
  +crianca: PositiveIntegerField(default=0)
  +check_in: DateField
  +check_out: DateField
  +quarto: TextField
  +rest_dia: DateField
  +rest_hora: TimeField
}

class funcionario {
  +nome: CharField(200)
  +cargo: CharField(200)
}

class timer_corrida {
  +date: DateTimeField
}

AbstractUser <|-- User
User "1" <-- "0..*" BlogPost : author
```


