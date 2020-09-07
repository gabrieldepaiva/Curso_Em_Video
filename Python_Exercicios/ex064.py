n = int(input('Digite um número [999 para parar]: '))
n1 = 0
c = 0
while n != 999:
    n1 = n1 + n
    c += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(c,n1))