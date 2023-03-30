# Biblioteca de expressões regulares
import re 
from django.contrib import messages
from django.contrib.messages import constants


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
