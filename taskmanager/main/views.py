from django.shortcuts import render
from .models import Task
# Create your views here. шаблоны


def index(request):
    tasks = Task.objects.all() #получаем объекты на главную страницу
    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, "main/about.html")
