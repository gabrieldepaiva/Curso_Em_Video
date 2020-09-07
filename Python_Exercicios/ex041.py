idade = int(input('Digite sua idade - '))
print()
if idade < 9:
    print('Mirim')
elif 9 <= idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <= 20:
    print('Senior')
elif idade > 20:
    print('Master')