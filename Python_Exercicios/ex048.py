n = int(input('Digite um número inteiro - '))
cont = 0
soma = 0
for cada_numero in range (1,n,2):
    if cada_numero % 3 == 0:
        cont = cont + 1
        soma = soma + cada_numero
print('A quantidade de números ímpares divididos por 3 entre 0 a {} é {}, sendo que a soma entre eles é {}.'.format(n,cont,soma))