v = 'Sequência de Fibonacci'
t = len(v)
print('-'*t)
print('Sequência de Fibonacci')
print('-'*t)
n = int(input('Digite a quantidade de termos - '))
t0 = 0
t1 = 1
c = 2
print(t0,end='')
print(' -> {}'.format(t1),end='')
while c != n:
    t2 = t0 + t1
    t0 = t1
    t1 = t2
    c += 1
    print(' -> {}'.format(t2),end='')
