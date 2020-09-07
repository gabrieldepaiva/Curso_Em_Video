preco = float(input('Digite o preço do produto - '))
print()
print('''Para o preenchimento do próximo campo seguir as instruções abaixo:
      Digite 1 para pagamento em dinheiro ou cheque
      Digite 2 para pagamento em cartão de crédito''')
print()
forma = int(input('Digite o código da forma de pagamento - '))
print()
if forma == 2:
    condicao = int(input('Digite a quandidade de parcelas - '))
    if condicao == 1:
        print('O produto terá o custo de R$ {:.2f}'.format(preco*0.90))
    elif condicao == 2:
        print('O produto terá duas parcelas de R$ {:.2f} custando R$ {:.2f} no total.'.format(preco/2,preco))
    elif condicao >= 3:
        print('O produto terá {:.0f} parcelas de R$ {:.2f} custando R$ {:.2f} no total.'.format(condicao,(preco*1.20)/condicao,preco*1.20))
elif forma == 1:
    print('O produto terá o custo de R$ {:.2f}.'.format(preco*0.90))
print()