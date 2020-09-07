from datetime import date
ano = date.today().year
nascimento = int(input('Digite o ano de nascimento - '))
if ano - nascimento > 18:
    print('Já passaram {} anos de se alistar no exército.'.format(ano - (nascimento+18)))
elif ano - nascimento == 18:
    print('Está em tempo de se alistar no exército')
else:
    print('Ainda não está na hora de se alistar no exército, mas faltam {} anos.'.format((nascimento+18)-ano))