numlist = []
n = int(input('Cadastre um número - '))
numlist.append(n)
resp = input('Quer cadastrar outro? -> [S/N] - ').strip().upper()[0]
while resp == 'S':
    n = int(input('Cadastre um número - '))
    if n not in numlist:
        numlist.append(n)
    resp = input('Quer cadastrar outro? -> [S/N] - ').strip().upper()[0]
numlist = sorted(numlist)
print()
print('Os valores digitados foram ',end='')
for num in numlist:
    print(num,end=' ')
print('.')