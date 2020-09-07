''' primeiro preciso declarar a variável
    depois fazer a estrutura de repetição, enquanto n for diferente de 999 ele vai pedir outro número
    enquanto vai pedindo outro número, ele vai somando o novo número e contando quantos números foram digitados
    no final, fazer a frase final com o novo método '''
n = int(input('Digite um número - [999 para encerrar] - '))
c = 1
if n == 999:
    print('Programa Encerrado sem digitar nenhum número.')
else:
    while n != 999:
        n1 = int(input('Digite outro número - [999 para encerrar] - '))
        if n1 == 999:
            break
        else:
            c += 1
            n = n + n1
print(f'Foram digitados {c} números e a soma deles foi {n}.')

