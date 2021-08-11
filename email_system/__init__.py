##### Built-in packages
import smtplib, ssl
#### Local packages
from private.credentials import email, password

def login_send(message_function):
    def login(*args, **kwargs):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.zoho.com', 465, context = context) as smtp:
            smtp.ehlo()
            try:
                smtp.login(email, password)
            except:
                return 0
            else:
                message = message_function(*args, **kwargs)
                smtp.send_message(message)
    return login