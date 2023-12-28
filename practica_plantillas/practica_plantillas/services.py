import requests
import logging

def generarRequest(url, parametros={}):
    response = requests.get(url, params=parametros)
    
    if response.status_code == 200:
        return response.json()


def get_imagen(parametros={}):
    respuesta = generarRequest('https://picsum.photos/v2/list', parametros)
    print(respuesta)
        
    return respuesta