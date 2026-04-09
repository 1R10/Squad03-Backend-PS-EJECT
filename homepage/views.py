from django.shortcuts import render, redirect
from .models import Hospedes
# aqui vai renderizar o html aparentemente ~Ryan

def index(request):
    return render(request, 'index.html')

def reservar(request):
    if request.method =='POST': # por padrão é GET ~Ryan
        print("POST recebido:", request.POST)
        name      = request.POST.get('name')
        check_in  = request.POST.get('check-in')
        check_out = request.POST.get('check-out')
        adults    = request.POST.get('amount-adult') or 0
        kids      = request.POST.get('amount-child') or 0
        f1_Team   = request.POST.get('equipe-f1')
        mail      = request.POST.get('email')
        p_number  = request.POST.get('phone')        
        
        reserva   =  Hospedes(
                    nome        = name, 
                    adulto      = int(adults), 
                    crianca     = int(kids),
                    check_in    = check_in, 
                    check_out   = check_out,
                    quarto      = f1_Team,
                    email       = mail,
                    telefone    = p_number
                    #rest_data  = nomedocoisadoretaurante,
                    #rest_hora  = nomehorarestaurante,
                      )
                    
        reserva.save()
        return redirect('homepage')
    

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')