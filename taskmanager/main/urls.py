from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-is', views.about, name='about')
]
