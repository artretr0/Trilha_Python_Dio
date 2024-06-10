# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

# Módulo 're' que fornece operações com expressões regulares.
import re

def validate_numero_telefone(phone_number):

    pattern = r"\(\d{2}\) 9\d{4}-\d{4}"
    # O 're.match()' retorna um objeto 'match' se houver correspondência no início da string, caso contrário, retorna 'None'.
    if re.match(pattern, phone_number) == 'match':
        print("telefone válido")
    else:
        print("telefone válido")
    
# Solicita ao usuário que insira um número de telefone e armazena o valor fornecido na variável 'phone_number'.
phone_number = input()  

validate_numero_telefone(phone_number)
