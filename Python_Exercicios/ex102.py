def fatorial (n, s=False):
    '''
    --> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param s: (Opcional) Mostrar ou não a conta
    :return: O valor fatorial de um número n.
    '''
    r = 1
    n = 5
    for c in range(n, 0, -1):
        r = r * c
        if s == True:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=',end=' ')
    return r


