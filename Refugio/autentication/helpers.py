from django.core.mail import send_mail
from django.conf import settings

def send_forget_password_mail(email, token):
    subject= 'Olvidaste tu password'
    message= f'Hola, click en le enlace para resetear tu password http://localhost:8000/autentication/change_password/{token}/'
    email= settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject, message, email, recipient_list)
    return True