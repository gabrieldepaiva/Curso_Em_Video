sal = float(input('Insira aqui seu salário atual - R$ '))
print('{:=^40}'.format('Cálculo de Reajuste Salarial'))
if sal <= 1250:
    print('Seu salário de R$ {:.2f} será reajustado para R$ {:.2f}.'.format(sal,sal*1.15))
else:
    print('Seu salário de R$ {:.2f} será reajustado para R$ {:.2f}.'.format(sal,sal*1.1))
