players = []
grupo = dict()
gols = []
somagol = 0
resp = 'S'
while resp in "Ss":
    grupo['jogador'] = input('Nome do jogador - ')
    partidas = int(input(f'Quantas partidas {grupo["jogador"]} jogou? - '))
    for n in range (1,partidas+1):
        gols.append(int(input(f'Quantos gols na partida {n}? - ')))
    for g in gols:
        somagol += g
    grupo['gol'] = gols.copy()
    gols.clear()
    grupo['total'] = somagol
    somagol = 0
    players.append(grupo.copy())
    resp = input('Deseja continuar? - ').strip().upper()[0]
print('-='*30)
print(f'{"Cod":15}{"Nome":<15}{"Gols":<15}{"Total":<15}')
print('-'*60)
for loc,j in enumerate(players):
    print(f'{loc}',end='              ')
    for d in j.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] - '))
    if busca == 999:
        break
    elif busca >= len(players):
        busca = int(input('Erro! Mostrar dados de qual jogador? [999 para parar] - '))
    else:
        print(f'Levantamento do jogador {players[busca]["jogador"]}:')
        for i,g in enumerate(players[busca]["gol"]):
            print(f'    No jogo {i+1} ele fez {g} gols.')
