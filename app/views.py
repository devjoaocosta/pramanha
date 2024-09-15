from django.shortcuts import render
from django.http import HttpResponse
from .models import Tarefa
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicial(req):
    return render(req, "app/inicial/index.html")


def entrar(req):
    if req.method == "GET":
        return render(req, "app/entrar/index.html")
    else:
        username = req.POST.get('username')
        senha = req.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(req, user)
            return HttpResponse('autenticado')
        else:
            return HttpResponse('email ou senha invalidos')

    

def registrar(req):
    if req.method == "GET":
        return render(req, "app/registrar/index.html")
    else:
        username = req.POST.get('username') 
        email = req.POST.get('email') 
        senha = req.POST.get('senha') 
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse('Este nome já está cadastrado')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()


        return HttpResponse('usuário cadastrado com sucesso')


@login_required(login_url='/auth/entrar')
def turma(req):
    return render(req, "app/turma/index.html")
    return HttpResponse('Você precisa estar logado para acessar essa página')

def tarefas(req):
    tarefas = Tarefa.objects.all
    return render(req, "app/tarefas/index.html", {"tarefas": tarefas})

