print('Sendo M - Masculino ou F - Feminino:')
sexo = str(input('Digite seu sexo - ')).upper()
print()
while sexo != 'M' and sexo != 'F':
    print('''Não emtendi, digite novamente sendo:
M - Masculino ou F - Feminino''')
    print()
    sexo = str(input('Digite seu sexo - ')).upper()
    print()