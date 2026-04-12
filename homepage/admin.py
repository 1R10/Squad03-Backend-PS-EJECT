from django.contrib import admin
from .models import Hospedes, timer_corrida,Suite,Restaurante

admin.site.register(Hospedes) #aparecer na admin
admin.site.register(timer_corrida) 
admin.site.register(Suite)
admin.site.register(Restaurante)