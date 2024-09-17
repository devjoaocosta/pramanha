from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    email = models.EmailField()
    senha = models.CharField(max_length=50, null=False, blank=False)

class Turma(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True)
    imagem = models.ImageField(null=True)
    alunos = models.ManyToManyField(Usuario)

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True)

class Tarefa(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_final = models.DateTimeField(null=False, blank=False)
    data_entrega = models.DateTimeField(null=True)

