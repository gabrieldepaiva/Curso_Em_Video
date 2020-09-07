n = 'Cálculo de Prestação de Casa'
print('-*-'*len(n))
print('{: ^84}'.format(n))
print('-*-'*len(n))
print()
casa = float(input('Insira o valor da casa - '))
salario = float(input('Insira o valor do salário mensal - '))
anos = int(input('Insira a quantidade de anos - '))
prestacoes = 12*anos
print()
comprometimento = ((casa/prestacoes)/salario)*100
if comprometimento <= 30:
    print('O valor da prestação mensal é R$ {:.2f}, comprometendo {:.2f}% da renda mensal, portanto aprovar o crédito.'.format(casa/prestacoes,comprometimento))
else:
    print('O valor da prestação mensal é R$ {:.2f}, comprometendo {:.2f}% da renda mensal, portanto, reprovar o crédito.'.format(casa/prestacoes,comprometimento))