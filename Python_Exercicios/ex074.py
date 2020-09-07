from random import randint
max = 0
a = randint(0,10)
b = randint(0,10)
c = randint(0,10)
d = randint(0,10)
e = randint(0,10)
tupla1 = (a,b,c,d,e)
print()
for num in tupla1:
    if num > max:
        max = num
min = max
for num in tupla1:
    if num < min:
        min = num
print(f'Os números sorteados pelo computador foram os seguintes: {tupla1}.')
print(f'O número máximo desse grupo é {max}.')
print(f'O número mínimo desse grupo é {min}.')