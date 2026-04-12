from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Hospedes, Restaurante
from Apollo_Hotel.settings import DEFAULT_FROM_EMAIL

@receiver(post_save, sender=Hospedes)
def enviar_email_reserva(sender, instance, created, **kwargs):
    if created:
        texto_email = {
            'name': instance.nome,
            'name_quarto': instance.quarto,
            'qtd_pessoas': int(instance.adulto or 0) + int(instance.crianca or 0),
            'qtd_adultos': instance.adulto,
            'qtd_criancas': instance.crianca,
            'data_checkin': instance.check_in,
            'data_checkout': instance.check_out,
            'data_restaurante': instance.rest_dia if instance.rest_dia else "Não reservado",
            'hour_restaurant': instance.rest_hora if instance.rest_hora else "--:--",
        }

        email_html = render_to_string('email.html', texto_email)
        text_content = strip_tags(email_html)

        send_mail(
            subject='Confirmação de Reserva - Apollo Hotel',
            message=text_content,
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            html_message=email_html,
            fail_silently=False,
        )

@receiver(post_save, sender=Restaurante)
def enviar_email_reserva_restaurante(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Confirmação de Reserva de Restaurante - Apollo Hotel',
            message=f'''
            Olá, {instance.nome}! Sua reserva para o restaurante foi recebida com sucesso.
            Detalhes:
             - Dia:   {instance.rest_dia}
             - Hora:  {instance.rest_hora} 
             - Grupo: {instance.grupo} Pessoas.
             - Local: No melhor restaurante de Mônaco.

            Agradecemos por escolher o Apollo Hotel!
            ''',
            from_email=DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )