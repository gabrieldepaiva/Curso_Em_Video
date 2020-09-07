lista = []
pares = []
impares = []
a = 'S'
while a == 'S':
    n = int(input('Digite um valor - '))
    lista.append(n)
    a = input('Quer continuar? - [S/N] - ').upper().strip()[0]
for num in lista:
    if num % 2 == 0:
        if num not in pares:
            pares.append(num)
    else:
        if num not in impares:
            impares.append(num)
print('Os valores digitados foram ',end='')
for num in lista:
    print(num,end=' ')
if len(pares) != 0:
    print('\nOs valores pares digitados foram ',end='')
    for nump in pares:
        print(nump,end=' ')
if len(impares) != 0:
    print('\nOs valores ímpares digitados foram ',end='')
    for numi in impares:
        print(numi,end=' ')
