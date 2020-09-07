'''a = int(input('Digite o primeiro valor - '))
b = int(input('Digite o segundo valor - '))
c = int(input('Digite o terceiro valor - '))
d = int(input('Digite o quarto valor - '))
print()
tupla1 = (a,b,c,d)
cont9 = 0
npar = 0
pos3 = 0
if 3 in tupla1:
    pos3 = tupla1.index(3) + 1
else:
    pos3 = 'Nenhuma'
for num in tupla1:
    if num == 9:
        cont9 += 1
    elif num % 2 == 0:
        npar += 1
print(f'Quantidade de números 9 - {cont9}')
print(f'Quantidade de números pares - {npar}')
print(f'Posição em que primeiro apareceu o número 3 - {pos3}.')'''

num = (int(input('Digite o primeiro valor - ')),
       int(input('Digite o segundo valor - ')),
       int(input('Digite o terceiro valor - ')),
       int(input('Digite o quarto valor - ')))
print()
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)}ª posição.')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares que foram digitados foram -', end = ' ')
for numero in num:
    if numero % 2 == 0:
        print(numero,end=' ')