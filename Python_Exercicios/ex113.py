def leiaint (txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('Erro! Por Favor digite um número inteiro válido.')
            continue
        else:
            return n



num = leiaint('Escreva um número - ')
print(f'O número digitado foi {num}.')

