medida1 = float(input('Qual a altura da parede em metros? '))
medida2 = float(input('Qual a largura da parede em metros? '))
area = medida1*medida2
print()
print('Sua parede tem a dimensão de {}m x {}m e sua área é de {:.2f}m².'.format(medida1,medida2,area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta, considerando que cada litro de tinta pinte 2m².'.format(area/2))