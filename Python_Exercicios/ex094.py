geral = []
cadastro = dict()
som_idade = 0
continuar = 'S'
while continuar == 'S':
    cadastro['nome'] = input('Nome - ')
    cadastro['sexo'] = input('Sexo [M/F]- ').upper().strip()[0]
    while cadastro['sexo'] not in 'MmFf':
        cadastro['sexo'] = input('Errado, tente novamente - [M/F]- ').upper().strip()[0]
    cadastro['idade'] = int(input('Idade - '))
    geral.append(cadastro.copy())
    continuar = input('Deseja continuar? - ').upper().strip()[0]
print('-='*30)
print(f'A) Ao todo, foram cadastradas {len(geral)} pessoas.')
for c in geral:
    som_idade += c['idade']
media = som_idade/len(geral)
print(f'B) A média de idade é de {som_idade/len(geral):.2f}')
print(f'C) As mulheres cadastradas foram: ',end='')
for d in geral:
    if d['sexo'] in 'Ff':
        print(d['nome'], end=' ')
print('\nD) Lista das pessoas que estão acima da média: ')
for p in geral:
    if p['idade'] >= media:
        print(f'==>{p["nome"]},{p["sexo"]:^5},{ p["idade"]:>3}')
