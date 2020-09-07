print('-*-'*8)
print('{: ^24}'.format('Jokempô'))
print('-*-'*8)
print()
print('''Instruções:
        Digite 1 para jogar "papel"
        Digite 2 para jogar "tesoura"
        Digite 3 para jogar "pedra"''')
print()
from random import randint
computador = (randint(1,3))
if computador == 1:
    computador = 'papel'
elif computador == 2:
    computador = 'tesoura'
else:
    computador = 'pedra'
usuario = int(input('Escolha uma opção conforme as instruções - '))
if usuario == 1:
    usuario = 'papel'
elif usuario == 2:
    usuario = 'tesoura'
else:
    usuario = 'pedra'
print()
print('Jo')
from time import sleep
sleep(1)
print('ken')
sleep(1)
print('po!')
print()
#papel ganha de pedra
if computador == 'papel' and usuario == 'pedra':
    print('O computador jogou {} e você jogou {}. O computador ganhou!'.format(computador,usuario))
elif usuario == 'papel' and computador == 'pedra':
    print('O computador jogou {} e você jogou {}. Você venceu!'.format(computador, usuario))
#tesoura ganha de papel
elif computador == 'tesoura' and usuario == 'papel':
    print('O computador jogou {} e você jogou {}. O computador ganhou!'.format(computador,usuario))
elif usuario == 'tesoura' and usuario == 'papel':
    print('O computador jogou {} e você jogou {}. Você venceu!.'.format(computador,usuario))
#pedra ganha de tesoura
elif computador == 'pedra' and usuario == 'tesoura':
    print('O computador jogou {} e você jogou {}. O computador ganhou!'.format(computador, usuario))
elif usuario == 'pedra' and computador == 'tesoura':
    print('O computador jogou {} e você jogou {}. Você ganhou!'.format(computador,usuario))
else:
    print('Tanto você quanto o computador jogaram {}. Empatou!'.format(usuario))

