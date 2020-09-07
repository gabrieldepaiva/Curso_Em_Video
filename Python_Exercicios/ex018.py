import math
angulo = float(input('Insira um angulo entre 0 e 90 graus - '))
angulo2 = math.radians(angulo)
tangente = math.tan(angulo2)
cosseno = math.cos(angulo2)
seno = math.sin(angulo2)
print ('Sua tangente é {:.2f}, seu cosseno é {:.2f} e seu seno é {:.2f}.'.format(tangente, cosseno, seno))