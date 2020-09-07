from datetime import date as hoje
lista = 0
maior = 0
menor = 0
for c in range(1,8):
    i = int(input('Digite o {}º ano - '.format(c)))
    if hoje.today().year - i <= 18:
        maior += 1
    else:
        menor += 1
print('Ao todo, tivemos {} pessoas maiores de idade.'.format(maior))
print('E também tivemos {} pessoas menores de idade.'.format(menor))



