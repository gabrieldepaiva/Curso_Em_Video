n = int(input('Digite um número - '))
resp = 'S'
soma = n
cont = 1
max = n
min = n
while resp == 'S':
    n1 = int(input('Digite outro número - '))
    soma = soma + n1
    cont = cont + 1
    if n1 > max:
        max = n1
    elif n1 < min:
        min = n1
    resp = str(input('''Quer digitar outro número?
[S] -> Sim 
[N] -> Não - ''')).upper()
    print()
media = soma / cont
print('A média entre os números digitados é {:.1f}.'.format(media))
print('O número {} foi o maior dentre os digitados.'.format(max))
print('O número {} foi o menor dentre os digitados.'.format(min))



