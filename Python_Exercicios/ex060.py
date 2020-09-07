n = int(input('Digite um número - '))
c = n
f = 1
while c > 1:
    f *= c
    c -= 1
print('O fatorial do número {} é o número {}.'.format(n, f))

