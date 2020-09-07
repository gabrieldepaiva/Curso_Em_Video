lista = []
lista2 = []
lista3 = []
lista4 = []
somapar = 0
somatercolun = 0
for c in range(0,3):
    lista2.append(int(input(f'Digite um valor para [0,{c}] - ')))
    lista.append(lista2[:])
    lista2.clear()
for c in range(0,3):
    lista3.append(int(input(f'Digite um valor para [1,{c}] - ')))
    lista.append(lista3[:])
    lista3.clear()
for c in range(0,3):
    lista4.append(int(input(f'Digite um valor para [2,{c}] - ')))
    lista.append(lista4[:])
    lista4.clear()
print('-='*30)
print(lista[0:3])
print(lista[3:6])
print(lista[6:9])
print('-='*30)
for loc, n in enumerate(lista):
    if n[0] % 2 == 0:
        somapar += n[0]
print(f'A soma dos valores pares é {somapar}.')
print(f'A soma dos valores da terceira coluna é {lista[2][0] + lista[5][0] + lista[8][0]}')
print(f'O maior valor da segunda linha é {max(lista[3:6])}.')
