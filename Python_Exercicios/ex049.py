print('=*='*8)
print('{: ^24}'.format('Cálculo da Tabuada'))
print('=*='*8)
print()
n = int(input('Escreva a tabuada desejada - '))
print()
for c in range(0,11):
    print('{} x {:2} = {:2}'.format(n,c,n*c))