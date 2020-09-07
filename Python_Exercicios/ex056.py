somaidade = 0
contador_de_idade = 0
idade_maxima = 0
nome_maximo = ''
for c in range (1,5):
    print('----- {}ª Pessoa -----'.format(c))
    nome = str(input('Digite seu nome - ')).strip()
    idade = int(input('Digite sua idade - '))
    sexo = str(input('Sexo [M/F] - ')).strip().upper()
    print()
    somaidade += idade
    if idade < 20 and sexo == 'F':
        contador_de_idade += 1
    if idade > idade_maxima and sexo == 'M':
        idade_maxima = idade
        nome_maximo = nome
    elif idade == idade_maxima and sexo == 'M':
        idade_maxima = idade
        nome_maximo += ' e {}'.format(nome)
mediaidade = float(somaidade) / 4
print('A média de idade do grupo é {:.0f} anos de idade.'.format(mediaidade))
print('Quantidade de mulheres abaixo de 20 anos - {}.'.format(contador_de_idade))
print('O nome do homem mais velhor é {}.'.format(nome_maximo))