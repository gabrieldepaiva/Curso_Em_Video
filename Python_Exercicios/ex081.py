lista = list()
a = 'S'
while a == 'S':
    n = int(input('Digite um valor - '))
    lista.append(n)
    a = input('Deseja continuar? - [S/N] - ').upper().strip()[0]
if 5 in lista:
    print('O valor 5 foi digitado e está na lista')
else:
    print('O valor não está na lista.')
print(f'O número de valores digitados na lista foram {len(lista)}')
print('A lista de valores ordenada de forma decrescente é a seguinte ',end='')
lista2 = reversed(sorted(lista))
for cadavalor in lista2:
    print(cadavalor,end=' ')