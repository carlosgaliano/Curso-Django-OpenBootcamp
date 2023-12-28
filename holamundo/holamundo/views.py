from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola Mundo")

def despedida(request):
    return HttpResponse("Despedida")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Es MAYOR de edad")
    else:
        return HttpResponse("Es MENOR de edad")