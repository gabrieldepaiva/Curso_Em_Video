"""from math import sqrt
cateto_oposto = float(input('Qual a medida do cateto oposto? - '))
cateto_adjacente = float(input('Qual a medida do cateto adjacente? - '))
print('Um triangulo retangulo que possui o cateto oposto medindo {} e o cateto adjacente medindo {} possui hipotenusa medindo {}.'.format(cateto_oposto,cateto_adjacente,sqrt(cateto_oposto**2+cateto_adjacente**2)))"""

from math import hypot
co = float(input('Qual a medida do cateto oposto? '))
ca = float(input('Qual a medida do cateto adjacente? '))
h = hypot(co,ca)
print ('Um triângulo retângulo com cateto oposto de comprimento {} e cateto adjacente com comprimento {} possui uma hipotenusa de comprimento {:.2f}.'.format(co,ca,h))