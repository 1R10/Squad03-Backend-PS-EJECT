from homepage.models import timer_corrida

def timer_c(request):
    return {
        'timer_corrida': timer_corrida.objects.first()
    }