def ficha (a='<desconhecido>',b=0):
    print(f'O jogador {a} fez {b} gol(s).')

n = input('Nome do Jogador: ')
g = input('Quantidade de Gols: ')
if g.isnumeric():
    int(g)
else:
    g = 0
if n.strip() == '':
    ficha(a='<desconhecido>')
else:
    ficha(n, g)


