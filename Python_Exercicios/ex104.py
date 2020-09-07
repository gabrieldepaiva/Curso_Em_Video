def leiaint(txt):
    n = str(txt).strip()
    while True:
        if n.isnumeric() == False:
            n = input('Erro! Número - ')
        else:
            n = int(n)
            break
    print(f'O número digitado foi {n}. ')

