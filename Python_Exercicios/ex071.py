print('='*30)
print('{:-^30}'.format(' Caixa '))
print('='*30)
print()
n = int(input('Qual o valor a ser sacado? - '))
total = n
cont = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        cont += 1
    else:
        if cont > 0:
            print(f'Foram usadas {cont} cédulas de R$ {ced},00.')
        if ced == 50:
            cont = 0
            ced = 20
        elif ced == 20:
            cont = 0
            ced = 10
        elif ced == 10:
            cont = 0
            ced = 5
        elif ced == 5:
            cont = 0
            ced = 1
        elif ced == 1:
            break
