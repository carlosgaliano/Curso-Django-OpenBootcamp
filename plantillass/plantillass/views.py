from django.http import HttpResponse
from django.shortcuts import render


def simple(request):
    #return HttpResponse("simple")
    return render(request, 'simple.html', {}) # se hace desde el archivo ya que se especifico dede el setting en plantillas DIR

def dinamico(request, name):
    #return HttpResponse('dinamico')
    categorias = ['codigo', 'diseño', 'publicidad']
    context = {'name': name, 'categorias': categorias}
    return render(request, 'dinamico.html', context)