lista = []
for c in range (0,5):
    n = int(input('Digite um valor - '))
    lista.append(n)
print('-'*50)
maior = max(lista)
menor = min(lista)
lista.index(maior)
lista.index(menor)
print()
print(f'Os valores digitados foram ',end=' ')
for c in lista:
    print(c,end=' ')
print(f'\nO maior valor digitado foi {maior}, que estava nas posições ',end='')
for pos, max_num in enumerate(lista):
    if maior == max_num:
        print(f'{pos + 1}ª',end=' ')
print(f'\nO menor valor digitado foi {menor}, que estava nas posições ',end='')
for pos, min_num in enumerate(lista):
    if min_num == menor:
        print(f'{pos + 1}ª',end=' ')