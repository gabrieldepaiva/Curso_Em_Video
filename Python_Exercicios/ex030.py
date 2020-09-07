n = int(input('Escreva um número inteiro - '))
if n < 0:
    n1 = n*(-1)
else:
    n1 = n*1
if n1 % 2 == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')