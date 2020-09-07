e = input('Validação de parenteses - ')
a = e.count('(')
f = e.count(')')
print()
if a == f:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está incorreta!')
