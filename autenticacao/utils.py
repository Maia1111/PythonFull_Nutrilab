# Biblioteca de expressões regulares
import re 
from django.contrib import messages
from django.contrib.messages import constants


def password_is_valid(request, senha, confirmar_senha):
     if len(senha) < 6:
            messages.error(request, 'Senha deve ter no minimo 6 caracteres.')
            return False
 
     if  not senha == confirmar_senha:
        messages.error(request, 'Confirmação de senha não confere com senha.')
        return False
     
     if not re.search('[A-Z]', senha):
          messages.error(request, 'Senha deve conter letras maiúsculas.')
          return False
     
     if not re.search('[a-z]', senha):
          messages.error(request, 'Senha deve conter letras minúsculas.')

     if not re.search('[1-9]', senha):
          messages.error(request, 'Senha deve conter números.')
          return False
     
     return True     
     

    

