boletim = []
notas = []
outro = "S"
cont = 1
while True:
    if outro == "S":
        boletim.append(input('Aluno - '))
        notas.append(float(input('Nota 1 - ')))
        notas.append(float(input('Nota 2 - ')))
        boletim.append(notas[:])
        notas.clear()
        outro = input('Quer continuar? [S/N] - ').upper().strip()[0]
        print()
    else:
        break
print()
print('-'*40)
print('No',end='')
print(f'{"Nome":^30}',end='')
print(f'{"Média":<30}')
print('-'*40)
for loc, aluno in enumerate(boletim):
    if loc % 2 == 0:
        print(cont,end='')
        print(f'{aluno:^30}',end='')
        cont += 1
    else:
        print(f'{(boletim[loc][0]+boletim[loc][1])/2:<30.1f}')
print('='*40)
opc = input('Mostrar nota de qual aluno? (999 para encerrar o programa) - ')
while True:
    if opc == '999':
        break
    else:
        print(f'O {opc} tirou {boletim[boletim.index(opc) + 1][0]} e {boletim[boletim.index(opc) + 1][1]}.')
        print('-' * 40)
        opc = input('Mostrar nota de qual aluno? (999 para encerrar o programa) - ')
