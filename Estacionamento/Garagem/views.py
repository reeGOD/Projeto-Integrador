from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Garagem.models import vagass
from Login.models import Profile

from django.contrib import auth ,messages

# Create your views here.

def garagem(request):
    item = vagass.objects.order_by("id")
    
    dados={
        'itens' : item,
    }
    return render(request,'Garagem.html', dados)

def CriarVaga(request):
    if request.method == 'POST':
        valor_total =  request.POST['valor_total']
        valor_total = int(valor_total)
        for i in range(valor_total):
            vaga = vagass.objects.create(iduser=0,validacao=False)
            vaga.save()
        return render(request,'index.html')
    return render(request,'CriarVaga.html')

def comprarvaga(request,valor):
    item = vagass.objects.get(id=valor)
    profiles = Profile.objects.get(user=request.user.id)
    item.iduser = profiles.id
    item.validacao = True
    item.save()
    
    return redirect('garagem')

