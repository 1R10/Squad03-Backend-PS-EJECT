from django.db import models

#python manage.py makemigrations/migrate

# Importante deixar os dados dos hóspedes separados para que o código escale melhor e seja mais independente de cada função ~Ryan

class Hospedes(models.Model):
    nome      = models.CharField(verbose_name='Nome completo', max_length= 200)
    adulto    = models.PositiveIntegerField(default=1) # Li um pouco e vi que assim só permite que receba 0 >= x. ~Ryan
    crianca   = models.PositiveIntegerField(default=0)
    check_in  = models.DateField() # vai receber em formato dd-mm-aaaa ~Ryan
    check_out = models.DateField()
    quarto    = models.TextField()
    email     = models.EmailField(default='', unique=False) 
    telefone  = models.CharField(default='', max_length=20)
    #rest_Data = models.DateField()
    #rest_hora = models.TimeField()
