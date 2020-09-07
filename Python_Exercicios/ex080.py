lista = []
for c in range(0,4):
    n = int(input('Digite um número - '))
    lista.append(n)
sorted(lista)
print('Os valores digitados foram ',end='')
for num in lista:
    print(num,end=' ')