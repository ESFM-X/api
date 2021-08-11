##### Installed packages
from flask_restful import Resource, abort  
##### Built-in packages
import string
from random import choice
from datetime import datetime
#### Local packages
from databases.esfm_x import tables
from databases import db
from private import  keys
from api_args import cdp as api_arguments
#### Constants
alphanum = string.ascii_uppercase + string.ascii_lowercase + string.digits


class cdp_data(Resource):
    ide = 'cdp'
    def post(self, key):
        if keys.validate(key):
            args = api_arguments.clubs_post_args.parse_args()
            print(args) 
            #  Verificar si el alumno es nuevo, si sí agregar a tabla alumnos
            
            query_by_boleta =  db.session.query(tables['alumnos']).filter_by(boleta = args['boleta']).first()
            
            if not query_by_boleta:
                print('El alumno no se encuentra registrado, registrando...')
                # Agregar registro a alumnos
                args_alumno = args.copy()
                del args_alumno['objetivo'], args_alumno['cursos']

                last_id = db.session.query(tables['alumnos']).order_by(tables['alumnos'].id.desc()).first().id
                current_id = last_id+1
                try:
                    new_alumno = tables['alumnos'](id = current_id,  **args_alumno)
                    db.session.add(new_alumno)
                    db.session.commit()
                except Exception as e: 
                    return {'error': str(e)}, 507
            else:
                current_id = query_by_boleta.id

            # Comprobar si el alumno no se ha registrado este periodo
            
            id_cursos_registrados = [r for r in db.session.query(tables[f'curso_alumno_{self.ide}'].id_curso).filter_by(periodo = args['periodo'], id_alumno = current_id )]
            if id_cursos_registrados:
                return {'error': 'Datos ya registrados para este periodo'}, 406

            # TODO: 
            # Verificar cupo
            # Permitir agregar cursos a registro

            # Generar token de registro ÚNICO por estudiante
            tokens = [r for r in db.session.query(tables[f'curso_alumno_{self.ide}'].token_registro).filter_by(periodo = args['periodo']).distinct()]
            token = ''.join(choice(alphanum) for _ in range(7) )
            while token in tokens:
                token = ''.join(choice(alphanum) for _ in range(7) )
            # Registrar curso por alumno
             
            for curso in args['cursos']:
                try:
                    new_relation = tables[f'curso_alumno_{self.ide}'](token_registro = token, 
                                                                    id_curso = curso, 
                                                                    id_alumno = current_id,
                                                                    destacado = False,
                                                                    periodo = args['periodo'],
                                                                    objetivo = args['objetivo'],
                                                                    fecha =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                                    )  
                    db.session.add(new_relation)
                    db.session.commit()
                except Exception as e: 
                    return {'error': str(e)}, 507
                else:
                    try:
                        curso  =  db.session.query(tables['cursos']).filter_by(id = curso).first()
                        curso.cupo = max(curso.cupo-1, 0)
                        db.session.commit()
                    except Exception as e: 
                        return {'error': str(e)}, 507
                    
            
            # TODO: Sistema Email Marketing 
                          
            # Regresar mensaje de éxito con token de registro generado
            return {'token': token}, 201
        else:
            abort(401, error =  'Parámetro Key inválido')
    def get(self, key):
        args = api_arguments.clubs_get_args.parse_args()
        if keys.validate(key):
            if args['datos'] == 'cursos':
                
                cursos =  db.session.query(tables['cursos']).filter_by(periodo = args['periodo']).all()
                respuesta = []
                for curso in cursos:
                    curso_limpio = curso.__dict__
                    del curso_limpio['_sa_instance_state']
                    respuesta.append(curso_limpio)
                return {'datos':respuesta}, 200
            elif args['datos'] == 'alumnos_anteriores':
                alumno =  db.session.query(tables['alumnos']).filter_by(boleta = args['boleta']).first()
                
                alumno = alumno.__dict__
                
                del alumno['_sa_instance_state']
                
                return {'datos':alumno}, 200

            elif args['datos'] == 'constancias':
                constancias =  db.session.query(tables['constancias']).filter_by(boleta = args['boleta']).all()
                if not constancias:
                    return {'error':'Constancias no encocntradas'},404
                respuesta = []
                for constancia in constancias:
                    constancia_limpia = constancia.__dict__
                    del constancia_limpia['_sa_instance_state']
                    curso = db.session.query(tables['cursos']).filter_by(id = constancia.id_curso).first()
                    constancia_limpia['curso'] = curso.nombre ## TODO: JOIN
                    respuesta.append(constancia_limpia)

                
                alumno = db.session.query(tables['alumnos']).filter_by(boleta = constancia.boleta).first()## TODO: JOIN
                
                return {'datos':respuesta, 'nombre': alumno.nombre}, 200

            elif args['datos'] == 'constancia':
                args['token'] = args['token'].replace('%C3%91', 'Ñ').replace('%C3%B1', 'ñ')
               
                constancia =  db.session.query(tables['constancias']).filter_by(token = args['token']).first()
                if not constancia:
                    return {'error':'Constancia no encocntrada'},404
                curso = db.session.query(tables['cursos']).filter_by(id = constancia.id_curso).first()## TODO: JOIN
                alumno = db.session.query(tables['alumnos']).filter_by(boleta = constancia.boleta).first()## TODO: JOIN

                constancia = constancia.__dict__
                del constancia['_sa_instance_state']
                constancia['curso'] = curso.nombre
                constancia['alumno'] = alumno.nombre
                return {'datos':constancia}, 200

            elif args['datos'] == 'constancias_correos':
                constancias =  db.session.query(tables['constancias']).filter_by(periodo = args['periodo']).all()
                respuesta = []
                for constancia in constancias:
                    constancia_limpia = constancia.__dict__
                    del constancia_limpia['_sa_instance_state']

                    alumno = db.session.query(tables['alumnos']).filter_by(boleta = constancia.boleta).first() ## TODO: JOIN
                    if not alumno:
                        print(constancia.boleta)
                        constancia_limpia['nombre'] = 'NOT ALUMNO'
                        constancia_limpia['email'] = 'NOT ALUMNO'
                    else:
                        constancia_limpia['nombre'] = alumno.nombre

                        constancia_limpia['email'] = alumno.email
                    respuesta.append(constancia_limpia)
                return {'datos':respuesta}, 200
            else:
                abort(404, error =  'Parámetro datos inválido')
        else:
            abort(401, error =  'Parámetro Key inválido')
