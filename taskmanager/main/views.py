from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here. шаблоны


def index(request):
    return HttpResponse("<h4>Hello</h4>")

def about(request):
    return HttpResponse("<h4>About</h4>")
