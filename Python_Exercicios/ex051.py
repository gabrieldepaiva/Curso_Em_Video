p_termo = int(input('Digite o primeiro termo de sua PA - '))
razao = int(input('Digite a razão de sua PA - '))
qdade_termos = int(input('Digite a quantidade de termos dessa PA - '))
print()
print('Os termos dessa PA são:')
soma = p_termo
print(p_termo, end=' ')
for n in range(1,qdade_termos):
    soma += razao
    print('-> {}'.format(soma), end=' ')
