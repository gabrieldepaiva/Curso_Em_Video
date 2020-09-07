from random import randint
from time import sleep
from operator import itemgetter
jogador = {'jogador 1': randint(0,10),
            'jogador 2': randint(0,10),
            'jogador 3': randint(0,10),
            'jogador 4': randint(0,10)}
for k, v in jogador.items():
    print(f'{k} - {v}')
    sleep(1)
jogador = sorted(jogador.items(), key=itemgetter(1),reverse=True)
print()
print('Ranking')
for l, v in enumerate(jogador):
    print(f'{l+1} Lugar: {v[0]} - {v[1]}')
