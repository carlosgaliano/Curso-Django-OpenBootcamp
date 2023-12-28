from django.shortcuts import render
from .services import get_imagen
import logging

def index(request):
    return render(request, 'index.html', {})

def portafolio(request):
    
    
    context = {
        'imagenes': get_imagen()
    }
    return render(request, 'portafolio.html', context )