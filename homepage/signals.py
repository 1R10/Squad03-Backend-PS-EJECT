from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Hospedes
from Apollo_Hotel.settings import DEFAULT_FROM_EMAIL

@receiver(post_save, sender=Hospedes)
def enviar_email_reserva(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Confirmação de Reserva - Apollo Hotel',
            message=f'''
            Olá, {instance.nome}!
            Sua reserva foi recebida com sucesso.
            
            Detalhes da reserva do quarto:


            Quarto:    {instance.quarto}
            Q. Pessoas: {int(instance.adulto) + int(instance.crianca)} ({instance.adulto} Adultos + {instance.crianca} crianças)
            Check-in:  {instance.check_in}
            Check-out: {instance.check_out}

            Restaurante:
            {instance.rest_dia} às {instance.rest_hora}
            


            Agradeçemos por escolher o Apollo Hotel!
            ''',
            from_email     = DEFAULT_FROM_EMAIL,
            recipient_list = [instance.email],
            fail_silently  = False,
        )