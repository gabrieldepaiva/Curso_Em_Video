print('{:=^50}'.format('Programa de Cálculo de Multas'))
n = float(input('Escreva a velocidade de um carro - '))
if n > 80:
    print('Ele foi multado')
    print('O valor a ser pago é de R$ {:.2f}.'.format((n-80)*7))
else:
    print('Ele não precisa ser multado.')