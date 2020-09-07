print('-'*40)
print('Jogo da Adivinhação')
print('-'*40)
n1 = int(input('Escreva um número inteiro de 0 a 5 - '))
if 0 <= n1 <= 5:
    from random import randint
    n2 = randint(0,5)
    print('O número escrito foi {}, o número que o computador escolheu foi {}.'.format(n1,n2))
    if n1 == n2:
        print('Você ganhou')
    else:
        print('Você perdeu')
else:
    print('Infelizmente não foi possível realizar o desafio.')