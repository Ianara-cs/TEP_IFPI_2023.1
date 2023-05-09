from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')

def valida_cadastro(request):
    username= request.POST['username']
    email = request.POST['email']
    password = request.POST['senha']
    senha2 = request.POST['senha2']

    try:
        user = User.objects.create_user(email=email, username=username, password=password)
        userAuthenticate = authenticate(request, username=user.username, password=password)
        print(userAuthenticate)
        if userAuthenticate is not None:
            auth_login(request, userAuthenticate)
            return redirect(request.POST.get('next', 'cadastra_perfil'))
    except:
        return redirect('cadastro')

def valida_login(request): 
    username = request.POST['username']
    password = request.POST['senha']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect(request.POST.get('next', 'cadastra_perfil'))
    else:
        print('erro de usuario ou password')
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')