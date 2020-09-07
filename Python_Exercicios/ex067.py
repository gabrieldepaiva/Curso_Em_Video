'''primeiro fazer o programa da tabuada em separado
depois colocar a condição se negativo ele vai parar'''
n = int(input('Digite um número [abaixo de 0 encerra o programa] - '))
while n > 0:
    if n < 0:
        break
    else:
        print(f'-----Tabuada do {n}-----')
        for cadanumero in range (0,11):
            n1 = n * cadanumero
            print(f'{n} x {cadanumero} = {n1}')
        print()
        n = int(input('Digite um número - [abaixo de 0 encerra o programa] - '))
print('Programa tabuada encerrado. Volte Sempre !')

