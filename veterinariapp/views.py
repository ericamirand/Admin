from django.shortcuts import render
from .models import Animais, Categoria
# Create your views here.

def index(request):
    return render('index.html')

def Animais(request):
    return render()

def Categoria(request):
    return render()