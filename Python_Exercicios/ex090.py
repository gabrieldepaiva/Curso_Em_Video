boletim = {'aluno':[],'media':[],'situacao':[]}
boletim['aluno'] = input('Escreva o nome do aluno - ')
boletim['media'] = float(input('Escreva a média do aluno - '))
if boletim['media'] >= 6:
    boletim['situacao'] = 'Aprovado'
else:
    boletim['situacao'] = 'Reprovado'
print('-='*30)
for k, v in boletim.items():
    print(f'- {k} é igual a {v}')
