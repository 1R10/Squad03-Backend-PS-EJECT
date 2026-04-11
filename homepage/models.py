from django.db import models

#python manage.py makemigrations/migrate

# Importante deixar os dados dos hóspedes separados para que o código escale melhor e seja mais independente de cada função ~Ryan

class Hospedes(models.Model):
    nome      = models.CharField(verbose_name='Nome completo', max_length= 200)
    email     = models.EmailField(verbose_name='E-mail', max_length=200)
    celular   = models.TextField() 
    adulto    = models.PositiveIntegerField(default=1) # Li um pouco e vi que assim só permite que receba 0 >= x. ~Ryan
    crianca   = models.PositiveIntegerField(default=0)
    check_in  = models.DateField() # vai receber em formato dd-mm-aaaa ~Ryan
    check_out = models.DateField()
    quarto    = models.TextField()
    rest_dia  = models.DateField(null=True, blank=True) # antes derrubava se não colocasse opcional ~Ryan
    rest_hora = models.TimeField(null=True, blank=True)

    
class Restaurante(models.Model):
    nome      = models.CharField(verbose_name='Nome completo', max_length= 200)
    email     = models.EmailField(verbose_name='E-mail', max_length=200)
    rest_dia  = models.DateField()
    rest_hora = models.TimeField()
    grupo     = models.PositiveBigIntegerField(default=1)


class timer_corrida(models.Model):
    date = models.DateTimeField()