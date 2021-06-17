from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. шаблоны


def index(request):
    return render(request, "main/index.html")


def about(request):
    return HttpResponse("<h4>About</h4>")
