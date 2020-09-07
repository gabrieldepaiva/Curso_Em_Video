def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha():
            print(f'Erro: {entrada} é um preço inválido.')
        else:
            valido = True
            return float(entrada)

leiadinheiro('100,50')