from random import randint as jogada_do_computador
vitorias = 0
while True:
    jogador = int(input('Digite um número de 0 a 10 - '))
    if jogador not in range(0,11):
        jogador = int(input('Por gentileza, digite um número de 0 a 10'))
    computador = jogada_do_computador(0,10)
    tipo = str(input('Par ou impar? - ')).strip().upper()[0]
    if (jogador + computador) % 2 == 0:
        if tipo in 'Pp':
            print(f'Você venceu! O computador jogou {computador} e você jogou {jogador}, somando {computador + jogador}.')
            vitorias += 1
            print()
        else:
            print('Você perdeu!')
            break
    elif (jogador + computador) % 2 == 1:
        if tipo in 'IiÍí':
            print(f'Você venceu! O computador jogou {computador} e você jogou {jogador}, somando {computador + jogador}.')
            vitorias += 1
            print()
        else:
            print('Você perdeu!')
            break
print()
print(f'Game Over! Você marcou {vitorias} pontos.')