# Biblioteca de expressões regulares
import re 
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import os 



def password_is_valid(request, senha, confirmar_senha):  

    is_valid = True

    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'Confirmação de senha não confere com senha.')
        is_valid = False

    if len(senha) < 6:
        messages.add_message(request, constants.ERROR, "Senha precisa ter no mínimo 6 caracteres!")
        is_valid = False

    if not re.search('[A-Z]', senha):
        messages.add_message(request, constants.ERROR, 'Senha deve conter letras maiúsculas.')
        is_valid = False

    if not re.search('[a-z]', senha):
        messages.add_message(request, constants.ERROR, 'Senha deve conter letras minúsculas.')
        is_valid = False

    if not re.search('[1-9]', senha):
        messages.add_message(request, constants.ERROR, 'Senha deve conter números.')
        is_valid = False   

    return is_valid


def email_html(path_template: str, assunto: str, para: list, **kwargs) -> dict:
    
    html_content = render_to_string(path_template, kwargs)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(assunto, text_content, settings.EMAIL_HOST_USER, para)

    email.attach_alternative(html_content, "text/html")
    email.send()
    return {'status': 1}
