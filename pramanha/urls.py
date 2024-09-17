"""
URL configuration for pramanha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import inicial
from app.views import tarefas
from app.views import turma
from app.views import home
from app.views import adicionar_disciplina, editar_disciplina, update_disciplina, delete_disciplina




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicial, name="inicial"),
    path('home', home, name="home"),
    path('tarefas', tarefas, name="tarefas"),
    path('auth/', include('app.urls')),
    path('turma', turma, name="turma"),
    path('adicionar_disciplina', adicionar_disciplina, name="adicionar-disciplina"),
    path('editar_disciplina/<int:id>', editar_disciplina, name='editar-disciplina'),
    path('update_disciplina/<int:id>', update_disciplina, name='update-disciplina'),
    path('delete_disciplina/<int:id>', delete_disciplina, name='delete-disciplina')



]

