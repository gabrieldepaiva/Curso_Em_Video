jogador = dict()
gols = []
somgols = 0
jogador['nome'] = input('Nome do Jogador: ')
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
if jogador['partidas'] == 0:
    print()
    print('Sem dados para análise.')
else:
    for c in range (1,jogador['partidas']+1):
        gols.append(int(input(f'Quantos gols na partida {c} - ')))
    jogador['gol'] = gols
    for g in gols:
        somgols += g
    print('-='*30)
    print(jogador)
    print('-='*30)
    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}.')
    print('-='*30)
    print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
    for loc,qdade in enumerate(gols):
        print(f'==> Na partida {loc + 1}, fez {qdade} gols.')
    print(f'Foi um total de {somgols}')