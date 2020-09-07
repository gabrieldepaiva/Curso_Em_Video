lista1 = []
lista2 = []
lista3 = []
lista4 = []
for c in range (0,3):
    lista4.append(int(input(f'Escreva um número para a posição 1x{c+1} - ')))
    lista1.insert(c,lista4[:])
    lista4.clear()
for c in range (0,3):
    lista4.append(int(input(f'Escreva um número para a posição 2x{c+1}- ')))
    lista2.insert(c,lista4[:])
    lista4.clear()
for c in range (0,3):
    lista4.append(int(input(f'Escreva um número para a posição 3x{c+1} - ')))
    lista3.insert(c,lista4[:])
    lista4.clear()
print(lista1)
print(lista2)
print(lista3)