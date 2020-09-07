n = int(input('Digite um número inteiro - '))
print('''Considere as opções abaixo para converter:
      [ 1 ] - Binário
      [ 2 ] - Hexadecimal
      [ 3 ] - Octal''')
print()
opcao = int(input('Escolha uma opção - '))
print()
if opcao == 1:
    print('O número {} convertido para binário é {}.'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número {} convertido para hexadecimal é {}.'.format(n, hex(n)[2:]))
elif opcao == 3:
    print('O número {} convertido para octal é {}.'.format(n, oct(n)[2:]))
else:
    print('Opção Invalida')