print('-*'*20)
print('{: ^40}'.format('Propriedade do Triângulo'))
print('-*'*20)
print()
lado1 = float(input('Digite uma medida - '))
lado2 = float(input('Digite outra medida - '))
lado3 = float(input('Digite a última medida - '))
print()
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print('É possível formar um triângulo do tipo equilátero.')
    elif lado1 == lado2 != lado3 or lado1 != lado2 == lado3 or lado1 == lado3 != lado2:
        print('É possível formar um triângulo do tipo isóceles.')
    else:
        print('É possível formar um triângulo do tipo escaleno.')
else:
    print('Não é possível formar um triângulo.')