import requests
from colorama import Fore, Back, Style

BASE = 'http://127.0.0.1:5000/'
key = '48c5a1d217fe85082464d2ca1e90a16d15464fabe20f8610d79b63aa58797b9b'
datos = [
    {'ruta':'cdp', 
     'args':{
            'nombre': 'Juan', 
            'email': 'juan123@gmail.com', 
            'carrera': 'Ing', 
            'semestre': 8, 
            'boleta': 1720331565, 
            'periodo': '2021-1',
            'objetivo': 'This python REST API tutorial will teach you how to build a python flask REST API. We will start by building a basic REST API then integrating that API with a flask SQL-Alchemy database. At the end of this video you will have a fully functioning REST API with python and flask.', 
            'cursos': [2,1],
            'semestres_ini':4,
            },
    'metodo':requests.post
    },
    {'ruta':'cdp', 
     'args':{
            'datos': 'cursos', 
            'periodo': '2021-1', 
            },
    'metodo':requests.get
    },
    
]

for dato in datos:
    print("#"*30, f'Ruta: {dato["ruta"]} Método: {dato["metodo"]}')

    print('Credenciales y datos correctos:', end = ' ')
    try: 
        response = dato['metodo'](BASE + f'{dato["ruta"]}/{key}', dato['args'] )
    except Exception  as e:
        print(f'Error en {dato["ruta"]}/{key}\n {e}\n\n\n')
    else:
        if str(response.status_code)[0] == '2':
            print(Fore.GREEN +'[OK]', Style.RESET_ALL)
        else:
            print(Fore.RED +'[NOT]', Style.RESET_ALL,  response.status_code, response.text)

    print('Falta de datos: ', end = ' ')
    response = dato['metodo'](BASE + f'{dato["ruta"]}/{key}' )
    if response.status_code == 400:
        print(Fore.GREEN +'[OK]', Style.RESET_ALL)
    else:
        print(Fore.RED +'[NOT]', Style.RESET_ALL, response.status_code, response.text)
    
    print('Método incorrecto: ', end = ' ')
    response =  requests.get(BASE + f'{dato["ruta"]}/{key}')
    if str(response.status_code)[0]  == '4':
        print(Fore.GREEN +'[OK]', Style.RESET_ALL)
    else:
        print(Fore.RED +'[NOT]', Style.RESET_ALL, response.status_code, response.text)

    print('Llave incorrecta: ', end = ' ')
    response =  requests.post(BASE + f'{dato["ruta"]}/{key}das')
    if response.status_code == 401:
        print(Fore.GREEN +'[OK]', Style.RESET_ALL)
    else:
        print(Fore.RED +'[NOT]', Style.RESET_ALL, response.status_code, response.text)
    print(Style.RESET_ALL)
    print("\n\n\n")