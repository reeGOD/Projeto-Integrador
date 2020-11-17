from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request,'index.html')

def Sobre(request):
    return render(request,'Sobre.html')

def Contato(request):
    return render(request,'Contato.html')