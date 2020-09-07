from random import randint

def sorteia(lista):
    for c in range (0, 5):
        lista.append(randint(0, 10))

def somapar(lista):
    tot = 0
    for c in lista:
        if c % 2 == 0:
            tot += c
    print(tot)


numeros = []
sorteia(numeros)
print(numeros)
somapar(numeros)