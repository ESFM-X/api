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
    correo_html = open("./email_system/templates/hackathon/verificacion_bienvenida.html", "r").read()
    message.add_alternative(correo_html.format(to =to, name=name, id=id, email_encrypted= email_encrypted), subtype= 'html')
    return message