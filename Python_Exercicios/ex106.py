r = 's'
while r == 's':
    help(input('Escreva o comando - '))
    r = input('Quer continuar [s/n] - ').strip().lower()[0]
print('Fim do Programa!')