print('{:-^50}'.format('Programa de Cálculo de Preço'))
n = int(input('Insira uma distância em Km - '))
if n < 200:
    print('O preço a ser cobrado pela passagem é R$ {:.2f}.'.format(n*0.5))
else:
    print('O preço a ser cobrado pela passagem é de R$ {:.2f}.'.format((n*0.4)))