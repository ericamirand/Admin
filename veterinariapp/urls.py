from django.urls import path
from .models import Animais, Categoria

urlpatterns = [
    path('', Animais, name='Animais'),
    path('', Categoria, name='Categoria'),
]