cadastros = []
pessoa = []
ppesadas = []
pleves = []
lista2 = []
continuar = nome = 'S'
print('='*50)
print(f'{"Cadastro de Clientes":^50}')
print('='*50)
while True:
    if continuar == 'S':
        pessoa.append(input('Escreva o nome - '))
        pessoa.append(float(input('Escreva o peso - ')))
        cadastros.append(pessoa[:])
        pessoa.clear()
        continuar = input('Deseja cadastrar outra pessoa? [S/N] - ').upper().strip()[0]
        print('-'*50)
    else:
        break
for p in cadastros:
    lista2.append(p[1])
max = max(lista2)
min = min(lista2)
for q in cadastros:
    if q[1] == max:
        ppesadas.append(q[0])
for r in cadastros:
    if r[1] == min:
        pleves.append(r[0])
print(f'As pessoas mais pesadas são as seguintes - {ppesadas}')
print(f'As pessoas mais leves são as seguintes - {pleves}')
print(f'O número de pessoas cadastradas foram {len(cadastros)}')
