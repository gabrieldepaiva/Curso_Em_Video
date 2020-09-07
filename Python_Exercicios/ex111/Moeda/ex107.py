def aumentar (n,p):
    '''
    -> Aumentar um número pela sua porcentagem
    :param n: Número a ser aumentado
    :param p: Porcentgem pela qual ele vai ser aumentado
    :return: Resultado final
    '''
    a = n + (n * (p/100))
    return a

def diminuir (n,p):
    '''
    -> Diminuir um número pela sua porcentagem
    :param n: Número a ser diminuido
    :param p: Porcentgem pela qual ele vai ser diminuido
    :return: Resultado final
    '''
    a = n - (n * (p/100))
    return a

def dobro (n):
    '''
    -> Dobro de um número
    :param n: Numero a ser sobrado
    :return: Dobro do número digitado.
    '''
    d = n * 2
    return d

def triplo (n):
    '''
    -> Metade de um número
    :param n: Numero a ser tratado
    :return: Metade do número digitado
    '''
    d = n / 2
    return d

def moeda (n,c = False):
    '''
    -> Serve para formatar um número em estilo monetário
    :param n: Número a ser formatado
    :param c: True formata o número em forma monetária
    :return: Valor formatado
    '''
    if c == True:
        f = "R$" + f' {n:.2f}'.replace('.',',')
        return f
    else:
        return n

def resumo (n,p):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)

    a = 'Preço Analisado:'
    b = 'Dobro do Preço:'
    c = 'Metade do Preço:'
    d = f'{p}% de aumento'
    e = f'{p}% de diminuição'

    print('Preço Analisado:',end='')
    print(f'{moeda(n,True):>14}')

    print('Dobro do Preço:',end='')
    print(f'{moeda(dobro(n),True):>15}')

    print('Metade do Preço:',end='')
    print(f'{moeda(triplo(n),True):>14}')

    print(f'{p}% de aumento:',end='')
    print(f'{moeda(aumentar(n,p),True):>16}')

    print(f'{p}% de diminuição:',end='')
    print(f'{moeda(diminuir(n, p), True):>13}')

    print('-'*30)
