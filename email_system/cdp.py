##### Built-in packages
from email.message import EmailMessage
#### Local packages
from . import login_send

enlaces_discord = {
    'Python-zh': ('https://discord.gg/mxBQnEV', 'Python from Zero to Hero'),
    'Ingenieria-datos':('https://www.discord.gg/jy6cJVt','Ingeniería de Datos'),
    'Pandas-ciencia':('https://discord.gg/NnpsUEy','Pandas para Ciencia de Datos'),
    'Ingenieria-datos':('https://www.discord.gg/jy6cJVt','Ingeniería de Datos'),
    'Matlab':('https://discord.gg/fxVk5x6h2B','MATLAB'),
    'Python-hg':('https://discord.gg/eDwjxNBAuh','Python from Hero to God'),
    'Criptografia':('https://discord.gg/xfvvzwTs7a','Criptografía Aplicada en C++'),
    'Wolfram':('https://discord.gg/z6hMkM4cjH','Wolfram Mathematica')

}

@login_send
def send(to, name, id, cursos):
    name = ''.join(word.capitalize() + ' ' for word in name.lower().split(' '))
    discord_tutorial = 'https://drive.google.com/file/d/1viSvFf8Vsq7yxMr2WQHdhqDKBKg2rc9z/view?usp=sharing'
    message = EmailMessage()
    message['Subject'] = 'Bienvenido al Club de Programación ESFM'
    message['From'] = 'Club de Programación ESFM <cdp@esfm-x.com>'
    message['To'] = to
    if len(cursos) == 1:
        curso = cursos[0]
        link, nombre_curso = enlaces_discord[curso]
        body = f"""  Hola {name}, bienvenido(a) al Club de Programación ESFM. \n\n 
                    Tu ID de registro es: {id} \n\n 
                    ¡Nos alegra que te intereses en nuestro curso {curso}! 
                    Te enviamos el link de la plataforma que ocuparemos para las sesiones: \n 
                                        {link} \n
                    Si no estás familiarizado con Discord, te adjuntamos una guía que preparamos: \n
                                        {discord_tutorial}\n\n """
        discord = f"""<p>Nos alegra que te intereses en nuestro curso {nombre_curso}. 
                         Te enviamos el link de la plataforma que ocuparemos para las sesiones: 
                         <a href = "{link}" style="color: #f9a836;"> Discord </a>.  
                      </p>
                        """
    else:
        
        links = ''
        for curso in cursos:
            link, nombre_curso = enlaces_discord[curso]
            links += f''' <br><li> <a href ="{link}" target="_blank" style = "color: #f9a836;"> {nombre_curso}</a> </li> '''
        body = f"""  Hola {name}, bienvenido(a) al Club de Programación ESFM. \n\n 
                    Tu ID de registro es: {id} \n\n 
                    ¡Nos alegra que te intereses en nuestro cursos! 
                    Te enviamos los enlaces de la plataforma que ocuparemos para las sesiones: \n 
                                        {links} \n
                    Si no estás familiarizado con Discord, te adjuntamos una guía que preparamos: \n
                                        {discord_tutorial}\n\n """
        discord = f"""<p>Nos alegra que te intereses en nuestro cursos. 
                         Te enviamos los enlaces de la plataforma que ocuparemos para las sesiones: 
                         {links} 
                      </p>
                        """
    message.set_content(body)
    correo_html = open("./email_system/templates/cdp/registro_bienvenida.html", "r").read()
    message.add_alternative(correo_html.format(name = name, id = id, discord = discord, discord_tutorial = discord_tutorial), subtype= 'html')
    return message


# def send(to,name,ide,curso):
#     name = ''.join(word.capitalize() + ' ' for word in name.lower().split(' '))
#     discord_tutorial = 'https://drive.google.com/file/d/1viSvFf8Vsq7yxMr2WQHdhqDKBKg2rc9z/view?usp=sharing'
#     if len(curso)==1:
#         curso = curso[0]
#         if curso == 'Python-zh':
#             link = 'https://discord.gg/mxBQnEV'
#             curso = 'Python from Zero to Hero'
#         elif curso == 'Ingenieria-datos':
#             link = 'https://www.discord.gg/jy6cJVt'
#             curso = 'Ingeniería de Datos'
#         elif curso == 'Pandas-ciencia':
#             link = 'https://discord.gg/NnpsUEy'
#             curso = 'Pandas para Ciencia de Datos'
#         elif curso == 'Matlab':
#             link = 'https://discord.gg/fxVk5x6h2B'
#             curso = 'MATLAB'
#         elif curso == 'Python-hg':
#             link = 'https://discord.gg/eDwjxNBAuh'
#             curso = 'Python from Hero to God'
#         elif curso == 'Criptografia':
#             link = 'https://discord.gg/xfvvzwTs7a'
#             curso = 'Criptografía Aplicada en C++'
#         elif curso == 'Wolfram':
#             link = 'https://discord.gg/z6hMkM4cjH'
#             curso = 'Wolfram Mathematica'
        
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL('smtp.zoho.com', 465, context = context) as smtp:
#             smtp.ehlo()
#             try:
#                 smtp.login(email, password)
#             except:
#                 return 0
#             else:
#                 body = "Hola {}, bienvenido(a) al Club de Programación ESFM. \n\n Tu ID de registro es: {} \n\n ¡Nos alegra que te intereses en nuestro curso {}! Te enviamos el link de la plataforma que ocuparemos para las sesiones: \n {} . \nSi no estás familiarizado con Discord, te adjuntamos una guía que preparamos: \n{}\n\n ".format(name,ide,curso,link,discord_tutorial)
#                 test = ''
#                 discord = f"""       <p>Nos alegra que te intereses en nuestro curso {curso}. Te enviamos el link de la plataforma que ocuparemos para las sesiones: <a href = "{link}" style="color: #f9a836;">Discord</a>.  </p>
#                                         <p> Si no estás familiarizado con Discord, te adjuntamos una guía que preparamos: <a href = "{discord_tutorial}" style="color: #f9a836;">Tutorial Discord</a>.  </p>
#                                         <br></br>"""
#                 msg = f'Subject: {subject}\n\n{body}'

#                 message = EmailMessage()
#                 message['Subject'] = subject
#                 message['From'] = sent_from
#                 message['To'] = to
#                 message.set_content(body)
#                 message.add_alternative(f"""
#                             <!DOCYPE html>
#                             <html>
#                                 <body style = "text-align: center;background-color: #343a40; color: #ffffff; font-family: Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif;">
#                                     <div style = "padding-top: 20px;padding-bottom:200px;margin-top:20px;margin-left:10;margin-right:10;">
#                                         <img src = "https://fotos.subefotos.com/a99ab1de3a4c1d7b7060458d2fc6e9a7o.png" style="width: 70%;margin-top:10px;margin-left:auto;margin-right:auto;display:block"/>
#                                         <br></br>
#                                         <h4>¡Hola {name}, bienvenido(a) al Club de Programación ESFM!</h4>
#                                         <h4 style ="color:#f9a836;">Tu ID de registro es: {ide} </h4>
#                                         <br></br>
#                                         {discord}
#                                         {test}
#                                     </div>
#                                 </body>
#                             </html>
                
#                 """, subtype= 'html')
                
#                 smtp.send_message(message)
#                 time.sleep(3)
#                 return 1
#     else:
#         cursos = ''
#         link = ''
#         for cu in curso:
#             if cu == 'Python-zh':
#                 link+= ' <br><li> • <a href ="https://discord.gg/mxBQnEV" target="_blank" style = "color: #f9a836;"> Python from Zero to Hero </a> </li> '
#                 cursos += ' Python from Zero to Hero*'
#             elif cu == 'Ingenieria-datos':
#                 link+= ' <br><li> • <a href ="https://www.discord.gg/jy6cJVt" target="_blank" style = "color: #f9a836;"> Ingeniería de Datos </a> </li> '
#                 cursos += ' Ingeniería de Datos*'
#             elif cu == 'Pandas-ciencia':
#                 link+= ' <br><li> • <a href ="https://discord.gg/NnpsUEy" target="_blank" style = "color: #f9a836;"> Pandas para Ciencia de Datos </a> </li> '
#                 cursos += ' Pandas para Ciencia de Datos*'
#             elif cu == 'Matlab':
#                 link+= ' <br><li> • <a href ="https://discord.gg/fxVk5x6h2B" target="_blank"  style = "color: #f9a836;"> MATLAB </a> </li> '
#                 cursos += ' MATLAB*'
#             elif cu == 'Python-hg':
#                 link += ' <br><li> • <a href ="https://discord.gg/eDwjxNBAuh" target="_blank"  style = "color: #f9a836;"> Python from Hero to God </a> </li>'
#                 cursos += ' Python from Hero to God*'
#             elif cu == 'Criptografia':
#                 link += ' <br><li> • <a href ="https://discord.gg/xfvvzwTs7a" target="_blank"  style = "color: #f9a836;"> Critografía Aplicada en C++ </a> </li>'
#                 cursos += ' Criptografía Aplicada en C++*'
#             elif cu == 'Wolfram':
#                 link += '<br><li> • <a href ="https://discord.gg/z6hMkM4cjH" target="_blank"  style = "color: #f9a836;"> Wolfram Mathematica </a> </li>'
#                 cursos += ' Wolfram Mathematica*'
        
#         context = ssl.create_default_context()
#         with smtplib.SMTP_SSL('smtp.zoho.com', 465, context = context) as smtp:
#             smtp.ehlo()
#             try:
#                 smtp.login(email, password)
#             except:
#                 return 0
#             else:
#                 cursof = ''
#                 for ca in cursos.split('*')[:-3]:
#                     cursof += ca + ','
#                 cursof+= cursos.split('*')[-3] + ' y'
#                 cursof += cursos.split('*')[-2]

#                 body = "Hola {}, bienvenido(a) al Club de Programación ESFM. \n\n Tu ID de registro es: {} \n\n ¡Nos alegra que te intereses en nuestro curso {}! Muy pronto nos pondremos en contacto contigo para invitarte a Microsoft Teams.".format(name,ide,curso)
#                 discord = f"""   
#                                     <p>Nos alegra que te intereses en nuestros cursos {cursof}. Te enviamos los enlaces de la plataforma que ocuparemos para las sesiones:
#                                         <ul style = "list-style: none; justify-content: center; color: #f9a836;" >
#                                             {link}
#                                         </ul>
                                    
#                                         </p>
#                             """
#                 message = EmailMessage()
#                 message['Subject'] = subject
#                 message['From'] = sent_from
#                 message['To'] = to
#                 message.set_content(body)
#                 message.add_alternative(f"""
#                             <!DOCYPE html>
#                             <html>
#                                 <body style = "text-align: center;background-color: #343a40; color: #ffffff; font-family: Open Sans, HelveticaNeue, Helvetica Neue, Helvetica, Arial, sans-serif;">
#                                     <div style = "padding-top: 20px;padding-bottom:200px;margin-top:20px;margin-left:10;margin-right:10;">
#                                         <img src = "https://fotos.subefotos.com/a99ab1de3a4c1d7b7060458d2fc6e9a7o.png" style="width: 70%;margin-top:10px;margin-left:auto;margin-right:auto;display:block"/>
#                                         <br></br>
#                                         <h4>¡Hola {name}, bienvenido(a) al Club de Programación ESFM!</h4>
#                                         <h4 style ="color:#f9a836;">Tu ID de registro es: {ide} </h4>
#                                         <br></br>
#                                         {discord}
#                                         <br></br>
#                                         <p> Si no estás familiarizado con Discord, te adjuntamos una guía que preparamos: <a href = "{discord_tutorial}" style="color: #f9a836;">Tutorial Discord</a>.  </p>
#                                         <br></br>
#                                         <p>En los próximos días te estaremos enviando un correo para validar tus datos y cupo de los cursos, para así confirmar tu ingreso al CdP ESFM. </p> 
#                                     </div>
#                                 </body>
#                             </html>
                
#                 """, subtype= 'html')
                
#                 smtp.send_message(message)
#                 time.sleep(3)
#                 return 1