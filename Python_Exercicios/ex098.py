from time import sleep
def contagem (inicio,fim,razao):
    if razao == 0:
        razao = 1
    if razao < 0:
        razao = razao * -1
    if fim < inicio:
        razao = razao * -1
        for c in range(inicio, fim-1, razao):
            print(c, end=' ')
            sleep(0.5)
        print()
    elif fim > inicio:
        for c in range(inicio, fim+1, razao):
            print(c, end=' ')
            sleep(0.5)
        print()


print('a) Contagem de 1 a 10 de 1 em 1:')
contagem(1,10,1)
print()
print('b) Contagem de 10 a 0 de 2 em 2:')
contagem(10,-1,2)
print()
print('c) Agora é com você:')
a = int(input('Começa em qual número - '))
b = int(input('Termina em qual número - '))
c = int(input('De quanto em quanto - '))
print('-'*(20))
contagem(a, b, c)



