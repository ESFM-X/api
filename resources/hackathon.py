##### Installed packages
from flask_restful import Resource, abort  
from api_args import hackathon as api_arguments
##### Built-in packages
import string
from random import choice
from datetime import datetime
#### Local packages
from databases.hackathon import tables, engine
from databases import db
from private import  keys
from fernet.utils import encrypt, decrypt
from email_system import hackathon as email_hackathon
#### Constants
alphanum = string.ascii_uppercase + string.ascii_lowercase + string.digits

session = db.create_scoped_session(
            options = {'bind': engine}
)
class hackathon_register(Resource):
    def post(self, key):
        """
        Inscribir a un equipo con sus integrantes
        """
        if keys.validate(key):
            args = api_arguments.hackathon_post_args.parse_args()
            # Registrar equipo
            ### Generar token de registro ÚNICO por equipo
            tokens = [r for r in session.query(tables['Equipos'].id).all()]
            token = ''.join(choice(alphanum) for _ in range(7) )
            while token in tokens:
                token = ''.join(choice(alphanum) for _ in range(7) )

            fecha =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            datos = self.clean(dict(args))
            args_equipo = datos.copy()
            del args_equipo['integrantes'], args_equipo['correos']
            try:
                new_equipo = tables['Equipos'](
                                id = token, 
                                fecha = fecha,
                                **args_equipo 
                                # nombre = args_equipo['nombre'],
                                # no_integrantes = args_equipo['no_integrantes'],
                                # categoria = args_equipo['categoria'],    
                            )
                session.add(new_equipo)
                session.commit()
            except Exception as e: 
                return {'error': str(e)}, 507
            # Registrar aspirantes
            for aspirante in datos['integrantes']:
                try:
                    new_aspirante = tables['Aspirantes'](
                                        id_equipo = token, 
                                        verificacion = False,
                                        **aspirante
                                    )
                    session.add(new_aspirante)
                    session.commit()
                except Exception as e: 
                    return {'error': str(e)}, 507
                else:
                    # Enviar email de verificacion
                    email_encrypted = encrypt(aspirante['email']).decode('UTF-8')
                    email_hackathon.send(aspirante['email'], token, aspirante['nombre'], email_encrypted)
            
            # Regresar mensaje de éxito con token de registro ded equipo generado
            return {'token': token}, 201
        else:
            abort(401, error =  'Parámetro Key inválido')

    def get(self, key):
        """
        Obtener correos unicos registrados
        """
        if keys.validate(key):
            args = api_arguments.hackathon_get_args.parse_args()
            try:
                correos = [r[0] for r in session.query(tables['Aspirantes'].email).all()]
                correos_repetidos = []
                args['correos'] = args['correos'].split('*')
                for correo in args['correos']:
                    correo = correo.replace('%40', '@')
                    if correo in correos:
                        correos_repetidos.append(correo)
                return {'datos': correos_repetidos}, 200
            except Exception as e: 
                return {'error': str(e)}, 507
        else:
            abort(401, error =  'Parámetro Key inválido')
    def put(self, key):
        """
        Verificar email de aspirantes
        """
        if keys.validate(key):
            args = api_arguments.hackathon_put_args.parse_args()
            email = decrypt(str.encode(args['email_encrypted']))
            aspirante  =  session.query(tables['Aspirantes']).filter_by(email = email).first()
            if not aspirante:
                return {'error': 'Email no encontrado. Si se trata de un error ponte en contácto a hackathon@esfm-x.com'}, 404
            if aspirante.verificacion: 
                return {'error': 'Email ya verificado'}, 400
            aspirante.verificacion = True
            session.commit()
            return {'mensaje': 'Email verificado con éxito'}, 200
        else:
            abort(401, error =  'Parámetro Key inválido')
    def clean(self, datos):
        data = {
        'no_integrantes': str(datos['cantidad']),
        'nombre':str(datos['nombre_equipo']),
        'categoria': str(datos['categoria']),
        'integrantes':[],
        'correos': []
        }
        for i in range(int(data['no_integrantes'])):
            data['integrantes'].append(
                {
                    'nombre': str(datos[f'nombre_{i}']),
                    'email': str(datos[f'correo_{i}']),
                    'escuela': str(datos[f'escuela_{i}']),
                    'especialidad': str(datos[f'especialidad_{i}'])
                }
            )
            data['correos'].append(datos[f'correo_{i}'])
        data['correos'] =  '*'.join(data['correos'])
        return data
        