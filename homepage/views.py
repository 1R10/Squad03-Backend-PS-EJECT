from django.shortcuts import render, redirect
from .models import Hospedes
# aqui vai renderizar o html aparentemente ~Ryan

def index(request):
    return render(request, 'index.html')

def reservar(request):
    if request.method =='POST': # por padrão é GET
        name      = request.POST.get('name')
        check_in  = request.POST.get('check-in')
        check_out = request.POST.get('check-out')
        adults    = request.POST.get('amount-adult')
        kids      = request.POST.get('amount-child')
        f1_Team   = request.POST.get('equipe-f1')
        
        
        reserva   =  Hospedes(
                    nome      = name, 
                    adulto    = adults, 
                    crianca   = kids,
                    check_in  = check_in, 
                    check_out = check_out,
                    quarto    =f1_Team )
                    
        reserva.save()
        return redirect('homepage')

def blog(request):
    return render(request, 'blog')

def about(request):
    return render(request, 'about.html')