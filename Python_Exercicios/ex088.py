from random import randint
from time import sleep
print('-'*50)
print(f'{"Joga na Mega Sena":^50}')
print('-'*50)
lista = []
n = int(input('Quantos jogos quer que eu gere? - '))
print(f'{"Gerando Jogos:":^50}')
for m in range (0, n):
    for intervalo in range (0,6):
        o = randint(1,60)
        while True:
            if o in lista and len(lista) < 6:
                o = randint(1,60)
            else:
                break
        lista.append(o)
    sleep(1)
    print(f'Jogo {m+1}: {sorted(lista)}')
    lista.clear()
