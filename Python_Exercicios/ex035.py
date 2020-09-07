lado1 = float(input('Digite a primeira medida do triângulo: '))
lado2 = float(input('Digite a segunda medida do triangulo: '))
lado3 = float(input('Digite a terceira medida do triângulo: '))
print()
if lado1 < lado2 < lado3:
    if lado2 - lado1 < lado3 < lado1 + lado2:
        print('É possível formar um triângulo com essas medidas.')
    else:
        print('Não é possível formar um triângulo com essas medidas.')
elif lado1 < lado3 < lado2:
    if lado3 - lado1 < lado2 < lado1 + lado3:
        print('É possível formar um triângulo com essas medidas.')
    else:
        print('Não é possível formar um triângulo com essas medidas')
elif lado2 < lado1 < lado3:
    if lado1 - lado2 < lado3 < lado1 + lado2:
        print('É possível formar um triângulo com essas medidas.')
    else:
        print('Não é possível formar um triângulo com essas medidas.')
elif lado2 < lado3 < lado1:
    if lado3 - lado2 < lado1 < lado2 + lado3:
        print('É possível formar um triângulo com essas medidas.')
    else:
        print('Não é possível formar um triângulo com essas medidas')
elif lado3 < lado1 < lado2:
    if lado1 - lado3 < lado2 < lado1 + lado3:
        print('É possível formar um triângulo com essas medidas.')
    else:
        print('Não é possível formar um triângulo com essas medidas.')
elif lado3 < lado2 < lado1:
    if lado2 - lado3 < lado1 < lado2 + lado3:
        print('É possível formar um triângulo com essas medidas.')
    else:
        print('Não é possível formar um triângulo com essas medidas.')