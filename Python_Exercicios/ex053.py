var = str(input('Digite uma frase - ')).strip().replace(' ','').lower()
caracteres = len(var)
nome = ''
for n in range(caracteres-1,-1,-1):
    inverso = (var[n])
    nome = nome + inverso
if var == nome:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')