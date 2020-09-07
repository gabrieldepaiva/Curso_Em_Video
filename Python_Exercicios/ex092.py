from datetime import date
cadastro = dict()
cadastro['Nome'] = input('Nome - ')
cadastro['Idade'] = date.today().year - int(input('Nascimento - '))
cadastro['CTPS'] = int(input('CTPS - '))
if cadastro['CTPS'] == 0:
    print(cadastro)
else:
    cadastro['Contratação'] = int(input('Ano da Contratação - '))
    cadastro['Salário'] = float(input(f'Salário - '))
    cadastro['Aposentadoria'] = cadastro['Contratação'] + 35
    print(cadastro)
print('Cadastro Consolidado')
for k, v in cadastro.items():
    print(f'{k}: {v}')
