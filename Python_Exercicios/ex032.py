from datetime import date
ano = int(input('Digite um ano qualquer (para ano atual digite o valor 0) - '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400:
    if ano % 100 == 0:
        print('É um ano bissexto e fevereiro tem 28 dias.')
    else:
        print('É um ano bissexto e fevereiro tem 29 dias.')
else:
    if ano % 400 == 0:
        print('Não é um ano bissexto e fevereiro tem 29 dias.')
    else:
        print('Não é um ano bisexto e fevereiro tem 28 dias.')