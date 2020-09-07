n1 = float(input('Escreva um número - '))
n2 = float(input('Escreva outro número - '))
soma = 0
mult = 0
maximo = 0
print('''Escolha uma das opções abaixo:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
print()
opcao = (int(input('Digite aqui - ')))
print()
while opcao != 5 :
    if opcao > 5 or opcao < 1:
        print('''Não entendi. 
        Escolha uma das opções abaixo:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
        print()
        opcao = (int(input('Digite aqui - ')))
    elif opcao == 1:
        soma = n1 + n2
        print('A soma é {}.'.format(soma))
        opcao = (int(input('Escolha outra opção - ')))
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação é {}.'.format(mult))
        opcao = (int(input('Escolha outra opção - ')))
    elif opcao == 3:
        maximo = max(n1,n2)
        print('Desses números, o maior é o {}.'.format(maximo))
        opcao = (int(input('Escolha outra opção - ')))
    elif opcao == 4:
        n1 = float(input('Escreva um número - '))
        n2 = float(input('Escreva outro número - '))
        print('''Escolha uma das opções abaixo:
        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa''')
        print()
        opcao = (int(input('Digite aqui - ')))
print('Programa Finalizado')
