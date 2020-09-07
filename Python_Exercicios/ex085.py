pares = []
impares = []
continuar = 'S'
while True:
    if continuar == 'S':
        elemento = int(input('Escreva um número qualquer inteiro - '))
        pares.append(elemento)
        continuar = input('Quer continuar - ').upper().strip()[0]
    else:
        break
for posicao, numeros in enumerate(pares):
    if numeros % 2 == 1 or numeros == 1:
        impares.append(numeros)
        pares.pop(posicao)
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')