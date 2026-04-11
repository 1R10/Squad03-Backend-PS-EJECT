from django.shortcuts import render, redirect
from .models import Hospedes, timer_corrida, Restaurante
# aqui vai renderizar o html aparentemente ~Ryan

def index(request):
    return render(request, 'index.html')

def reservar(request):
    if request.method =='POST': # por padrão é GET ~Ryan
        print("POST recebido:", request.POST)
        name      = request.POST.get('name')
        mail      = request.POST.get('email')
        phone     = request.POST.get('phone')
        check_in  = request.POST.get('check-in')
        check_out = request.POST.get('check-out')
        adults    = request.POST.get('amount-adult') or 1
        kids      = request.POST.get('amount-child') or 0
        f1_Team   = request.POST.get('equipe-f1')
        rest_date = request.POST.get('restaurant-date')
        rest_time = request.POST.get('restaurant-time')
        if rest_date == "":
            rest_date = None
        if rest_time == "0" or rest_time == "":
            rest_time = None
        
        
        reserva   =  Hospedes(
                    nome      = name,
                    email     = mail,
                    celular   = phone, 
                    adulto    = adults, 
                    crianca   = kids,
                    check_in  = check_in, 
                    check_out = check_out,
                    quarto    = f1_Team,
                    rest_dia  = rest_date,
                    rest_hora = rest_time,
                     )
                    
        reserva.save()
        referer = request.META.get('HTTP_REFERER', '/') # procura a url anterior a do forms. antes iria so pra homepage
        return redirect(referer)
        #return redirect('homepage')

def reservar_restaurante(request):
    if request.method =='POST': 
        print("POST recebido:", request.POST)

        name      = request.POST.get('restaurant-name')
        mail      = request.POST.get('restaurant-email')
        group     = request.POST.get('qtd-people')
        rest_date = request.POST.get('reserve-restaurant-date')
        rest_time = request.POST.get('reserve-restaurant-time')


        reserva_restaurante = Restaurante(
                    nome      = name,
                    email     = mail,
                    grupo     = group,
                    rest_dia  = rest_date,
                    rest_hora = rest_time,

        )

        reserva_restaurante.save()
        referer = request.META.get('HTTP_REFERER', '/') 
        return redirect(referer)

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def time(request):
    return render(request, 'time.html')