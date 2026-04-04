from django.db import models
#import datetime
#python manage.py makemigrations/migrate
class Hospedes(models.Model):
    nome    = models.CharField(verbose_name='Nome completo', max_length= 200)
    adulto  = models.PositiveIntegerField(default=1) # Li um pouco e vi que assim só permite que receba 0 >= x.
    crianca = models.PositiveIntegerField(default=0)

class Reserva(models.Model):
    hospede  = models.ForeignKey(Hospedes, on_delete=models.CASCADE) # uma reserva SEMPRE vai pertencer ao hóspede. sem hospede = deleta
'''    check_in  = models.DateTimeField(default=datetime.now) # não é now. Preciso ver como recebe do forms
    check_out = models.DateTimeField()'''

