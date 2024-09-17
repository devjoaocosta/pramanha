from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa, Disciplina
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
            return render(req, 'app/home/index.html')
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


        return render(req, 'app/entrar/index.html')


@login_required(login_url='/auth/entrar')
def turma(req):
    disciplinas = Disciplina.objects.all
    return render(req, "app/turma/index.html", {"lista_disciplinas": disciplinas})

@login_required(login_url='/auth/entrar')
def home(req):
    return render(req, 'app/home/index.html')

def tarefas(req):
    tarefas = Tarefa.objects.all
    return render(req, "app/tarefas/index.html", {"tarefas": tarefas})

def adicionar_disciplina(req):
    if req.method == "GET":
        return render(req, "app/adicionar_disciplina/index.html")
    else:
        nova_disciplina = Disciplina()
        nova_disciplina.nome = req.POST.get('nome')
        nova_disciplina.descricao = req.POST.get('descricao')
        nova_disciplina.save()


        return turma(req)
    
def editar_disciplina(req, id):
    disciplina = Disciplina.objects.get(id=id)
    return render(req, "app/editar_disciplina/index.html", {'disciplina': disciplina})


def update_disciplina(req, id):
        disciplina = Disciplina.objects.get(id=id)
        disciplina.nome = req.POST.get('nome')
        disciplina.descricao = req.POST.get('descricao')
        disciplina.save()
        return redirect(home)

def delete_disciplina(req, id):
    disciplina = Disciplina.objects.get(id=id)
    disciplina.delete()
    return redirect(home)
