print('='*30)
print('{: ^30}'.format(' Jogo da Adivinhação '))
print('='*30)
print()
from random import randint
computador = randint(0,10)
usuario = int(input('Escreva um número de 0 a 10 - '))
tentativas = 1
print()
while usuario < 0 or usuario > 10:
    print('Para o jogo funcionar é necessário digitar um número de 0 a 10')
    usuario = int(input('Tente novamente - '))
    print()
while usuario != computador:
    tentativas = tentativas + 1
    if usuario < computador:
        print('Computador pensou em um número maior que o seu!')
        usuario = int(input('Escreva novamente um número de 0 a 10 - '))
        print()
    elif usuario > computador:
        print('Computador pensou em um número menor que o seu!')
        usuario = int(input('Escreva novamente um número de 0 a 10 - '))
        print()
if tentativas == 1:
    print('Você ganhou com 1 tentativa! Parabéns!!! ')
else:
    print('Você ganhou. Foram necessárias {} tentativas'.format(tentativas))

