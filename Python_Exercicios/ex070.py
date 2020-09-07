produto = str(input('Escreva o nome do produto - '))
valor = float(input('Qual o valor do produto - '))
continuar = str(input('Deseja cadastrar outro produto? - [S/N] - ')).upper().strip()[0]
print()
total = valor
if valor > 1000:
    P_1000 = 1
else:
    P_1000 = 0
P_min = valor
barato = produto
while True:
    if continuar in 'Ss':
        produto1 = str(input('Escreva o nome do produto - '))
        valor1 = float(input('Qual o valor do produto - '))
        continuar = str(input('Deseja cadastrar outro produto? - [S/N] - ')).upper().strip()[0]
        print()
        total += valor1
        if valor1 > 1000:
            P_1000 += 1
        if valor1 < P_min:
            barato = produto1
            P_min = valor1
    else:
        break
print(f'{total} foi o total da compra.')
print(f'{P_1000} foi número de produtos cadastrados que custam acima de R$ 1.000,00')
print(f'O produto mais barato foi o {barato} que custou {P_min}.')