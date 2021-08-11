from flask_restful import reqparse

hackathon_post_args = reqparse.RequestParser()
arguments = [
    {'nombre':'nombre_equipo', 'type': str, 'help':'Nombre del equipo es requerido y de tipo str','required':True},
    {'nombre':'cantidad', 'type': int, 'help': 'Número de integrantes es requerido y de tipo int','required':True},
    {'nombre':'categoria', 'type': int, 'help': 'Categoría es requerido y de tipo int','required':False},
    ] + [
            {
                'nombre':f'nombre_{i}', 
                'type':str, 
                'help':'Nombre de aspirante es requerido y de tipo str',
                'required': False
            } for i in range(5)
    ] + [
            {
                'nombre':f'correo_{i}', 
                'type':str, 
                'help':'Correo de aspirante es requerido y de tipo str',
                'required': False
            } for i in range(5)
    ] + [
            {
                'nombre':f'escuela_{i}', 
                'type':str, 
                'help':'Escuela del aspirante es requerido y de tipo str',
                'required': False
            } for i in range(5)
    ] + [
            {
                'nombre':f'especialidad_{i}', 
                'type':str, 
                'help':'Especialidadd del aspirante es requerido y de tipo str',
                'required': False
            } for i in range(5)
    ]
    

for argument in arguments:
    hackathon_post_args.add_argument(argument['nombre'], 
                                 type = argument['type'], 
                                 help = argument['help'],
                                 required=argument['required']
                    )
hackathon_get_args = reqparse.RequestParser()
arguments = [
    {'nombre':'correos', 'type':str, 'help':'String de correos separados por "*" es requerido y de tipo list','required':True},
]

for argument in arguments:
    hackathon_get_args.add_argument(argument['nombre'], 
                                 type = argument['type'], 
                                 help = argument['help'],
                                 required=argument['required']
                    )

hackathon_put_args = reqparse.RequestParser()
arguments = [
    {'nombre':'email_encrypted', 'type':str, 'help':'Correo encriptado es requerido y de tipo str','required':True},
]

for argument in arguments:
    hackathon_put_args.add_argument(argument['nombre'], 
                                 type = argument['type'], 
                                 help = argument['help'],
                                 required=argument['required']
                    )