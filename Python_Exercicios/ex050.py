soma = 0
cont = 0
for item in range (1,7):
    n= int(input('Escreva o {}º número - '.format(item)))
    if n % 2 == 0:
        soma += n
        cont += 1
if cont == 0:
    print('Nenhum número par foi relacionado.')
elif cont == 1:
    print('Apenas um número par foi digitado e o valor é {}.'.format(soma))
else:
    print('Você digitou {} números pares e a soma entre eles é {}.'.format(cont, soma))
