from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here. шаблоны


def index(request):
    tasks = Task.objects.order_by('-id') #получаем все объекты на главную страницу по id
    return render(request, "main/index.html", {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, "main/about.html")


def create(request):
    error = ''
    if request.method == 'POST':
        # сохраняем данные
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной!'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "main/create.html", context)
