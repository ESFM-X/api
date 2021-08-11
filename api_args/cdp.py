from flask_restful import reqparse

clubs_post_args = reqparse.RequestParser()
arguments = [
    {'nombre':'nombre', 'type': str, 'help':'Nombre del estudiante es requerido y de tipo str','required':True},
    {'nombre':'email', 'type': str, 'help': 'Email del estudiante es requerido y de tipo str','required':True},
    {'nombre':'carrera', 'type': str, 'help': 'Carrera del estudiante es requerido y de tipo str','required':True},
    {'nombre':'semestres_ini', 'type': int, 'help': 'Semestre del estudiante es requerido y de tipo int','required':True},
    {'nombre':'boleta', 'type': int, 'help': 'Boleta del estudiante es requerido y de tipo int','required':True},
    {'nombre':'periodo', 'type': str, 'help': 'Periodo es requerido y de tipo str','required':True},
    {'nombre':'objetivo', 'type': str, 'help': 'Objetivo del estudiante es requerido y de tipo str','required':True},
    {'nombre':'cursos', 'type':list, 'help':'Lista de cursos es requerido y de tipo list','required':True},
]

for argument in arguments:
    clubs_post_args.add_argument(argument['nombre'], 
                                 type = argument['type'], 
                                 help = argument['help'],
                                 required=True
                    )

clubs_get_args = reqparse.RequestParser()
arguments = [
    {'nombre':'datos', 'type': str, 'help':'Nombre de datos que se solicita es requerido y de tipo str. Opciones: cursos, alumnos_anteriores','required':True},
    {'nombre':'periodo','type':str, 'help': 'Periodo es requerido y de tipo str','required':True},
    {'nombre':'boleta','type':int, 'help': 'Boleta es requerido y de tipo int','required':False},
    {'nombre':'token','type':str, 'help': 'Token de constancia es requerido y de tipo str','required':False}
]
for argument in arguments:
    clubs_get_args.add_argument(argument['nombre'], 
                                 type = argument['type'], 
                                 help = argument['help'],
                                 required=argument['required']
                    )
