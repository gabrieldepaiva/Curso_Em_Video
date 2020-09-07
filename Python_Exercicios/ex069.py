print('-'*30)
print('Cadastro de Pessoas')
print('-'*30)
prosseguir = 'S'
c_homens = 0
c_idade = 0
c_mulheresabaixode20 = 0
while True:
    if prosseguir == 'S':
        nome = str(input('Digite o nome - '))
        idade = int(input('Digite a idade - '))
        sexo = str(input('Digite o sexo - [M/F] - ')).strip().upper()[0]
        prosseguir = str(input('Deseja cadastrar mais alguem? - [S/N] - ')).strip().upper()[0]
        print('-'*30)
        if sexo in 'Mm':
            c_homens += 1
        if sexo in "Ff" and idade < 20:
            c_mulheresabaixode20 += 1
        if idade > 18:
            c_idade += 1
    else:
        break
print(f'Dessa relação de cadastros, {c_idade} pessoas tem mais de 18 anos, {c_homens} homens foram cadastrados e {c_mulheresabaixode20} mulheres com menos de 20 anos foram cadastradas.')