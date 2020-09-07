n = float(input('Digite o 1ª peso - '))
maximo = n
minimo = n
for i in range (2,6):
    n1 = float(input('Digite o {}ª peso - '.format(i)))
    if n1 > maximo:
        maximo = n1
    elif n1 < minimo:
        minimo = n1
print('O maior peso é {}.'.format(maximo))
print('O menor peso é {}.'.format(minimo))