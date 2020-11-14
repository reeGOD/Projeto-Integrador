from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Login.models import Profile
from django.contrib import auth ,messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('index')

def Login(request):
    if request.method == 'POST':
        usuario =  request.POST['username']
        senha = request.POST["password"]
        if usuario == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            print(usuario, senha)
            return render(request,'Login.html')
        if User.objects.filter(email=usuario).exists():
            nome = User.objects.filter(email=usuario).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('index')
            print(nome)
        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            print('Login realizado com sucesso')

            return redirect('index')

        return render(request,'Login.html')

    else:
        return render(request,'Login.html')
    return render(request,'Login.html')

def Cadastro(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        nasc = request.POST['nasc']
        gender = request.POST['gender']
        car = request.POST['car']
        license_plate = request.POST['license_plate']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confpassword = request.POST['confpassword']
        if len(user_name) < 3:
            return redirect('Cadastro')
        if not user_name.strip():
            print('O campo Username não pode ficar em branco')
            return redirect('Cadastro')
        if not first_name.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('Cadastro')
        if not last_name.strip():
            print('O campo sobrenome não pode ficar em branco')
            return redirect('Cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('Cadastro')
        if not nasc.strip():
            print('O campo  não pode ficar em branco')
            return redirect('Cadastro')
        if not phone.strip():
            print('O campo  não pode ficar em branco')
            return redirect('Cadastro')
        if not gender.strip():
            print('O campo  não pode ficar em branco')
            return redirect('Cadastro')
        if not car.strip():
            print('O campo  não pode ficar em branco')
            return redirect('Cadastro')
        if not license_plate.strip():
            print('O campo  não pode ficar em branco')
            return redirect('Cadastro')
        if password != confpassword:
            print('As senhas não são iguais')
            return redirect('Cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('Cadastro')
        if User.objects.filter(username=user_name).exists():
            print('Usuário já cadastrado')
            return redirect('Cadastro')
        user = User.objects.create_user(username=user_name, email=email, password=password,first_name=first_name, last_name =last_name)
        user.save() 
        user = auth.authenticate(request, username=user_name, password=password)
        auth.login(request, user)

        profile = Profile.objects.create(numero=phone,sexo=gender,user_id = request.user.id,aniversario=nasc,placacar=license_plate,car=car)
        profile.save()
        print('Usuário cadastrado com sucesso')
        return redirect('index')
    return render(request,'Register.html')
