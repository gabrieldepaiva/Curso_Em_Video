pt = int(input('Digite o primeiro termo da PA - '))
razao = int(input('Digite a razao da PA - '))
termos = int(input('Digite a quantidade de termos da PA - '))
c = 0
while termos != 0:
    while c < termos:
        print(pt, end=' ')
        c = c + 1
        pt = pt + razao
print('Programa Terminado')