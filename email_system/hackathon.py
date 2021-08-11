##### Built-in packages
from email.message import EmailMessage
import os
#### Local packages
from . import login_send

@login_send
def send( to, id, name, email_encrypted):
    message = EmailMessage()
    message['Subject'] = 'Bienvenido al Hackathon ESFM-X 2021' 
    message['From'] = 'Hackathon ESFM-X <hackathon@esfm-x.com>'
    message['To'] = to
    body = f"""¡Hola {name}! Has sido registrado al hackathon ESFM-X 2021 con éxito. 
                Necesitas verificar tu correo entrando dando clic al siguiente enlace: 
                https://hackathon.esfm-x.com/verificar/{email_encrypted} \n 
                ID de registro: {id}"""
    message.set_content(body)
    correo_html = open("./email_system/templates/hackathon/verificacion_bienvenida.html", "r", encoding = 'UTF-8').read()
    message.add_alternative(correo_html.format(to =to, name=name, id=id, email_encrypted= email_encrypted), subtype= 'html')
    return message

@login_send
def send_invitation( to, name):
    message = EmailMessage()
    message['Subject'] = 'Te invitamos al Hackathon ESFM-X 2021' 
    message['From'] = 'CdP ESFM <cdp@esfm-x.com>'
    message['To'] = to
    body = f"""¿Te gustaría crear o innovar algún proyecto dentro de tu institución? ¡Ésta es tu oportunidad! 🚀\n\n
                Participa en el Hackathon ESFM-X 2021 este 14 y 15 de agosto desarrollando soluciones digitales para tu escuela o a nivel institucional.\n

                No necesitas saber programar, y tampoco tener un equipo, basta con registrarte y nuestro algoritmo te asignará con personas que te ayudarán a ganar esta competencia. ¡Totalmente en línea!\n\n

                Tienes hasta el 13 de agosto para registrarte.\n\n
                Ingresa a https://hackathon.esfm-x.com para saber más.
                """
    message.set_content(body)
    correo_html = open("./email_system/templates/hackathon/invitacion.html", "r", encoding = 'UTF-8').read()
    message.add_alternative(correo_html.format(name=name), subtype= 'html')
    return message