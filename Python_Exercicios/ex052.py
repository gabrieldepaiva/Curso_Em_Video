n = int(input('Digite um número inteiro - '))
print()
divisibilidade = 0
for c in range (1,n+1):
    if n % c == 0:
        divisibilidade = divisibilidade + 1
if divisibilidade == 2:
    print('O número {} é um número primo'.format(n))
else:
    print('O número {} não é um número primo'.format(n))