print('-'*40)
print(f'{"lista de Produtos":^40}')
print('-'*40)
a = ('produto 1', 0.00,'produto 2', 0.00,'produto 3', 0.00,'produto 4', 0.00,
    'produto 5', 0.00,'produto 6', 0.00,'produto 7', 0.00,'produto 8', 0.00,
    'produto 9', 0.00,'produto 10', 0.00,)
for elemento in range(0,len(a)):
    if elemento % 2 == 0:
        print(f'{a[elemento]:.<30}',end='')
    else:
        print(f'{a[elemento]:.>7.2f}')
