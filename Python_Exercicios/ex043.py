peso = float(input('Digite aqui o seu peso - '))
altura = float(input('Digite aqui sua altura - '))
print()
imc = peso / altura ** 2
print()

if imc < 18.5:
    print('Abaixo do peso com IMC de {:.2f}.'.format(imc))
elif 18.5 <= imc <= 25:
    print('Peso Ideal com IMC de {:.2f}.'.format(imc))
elif 25 < imc <= 30:
    print('Sobrepeso com IMC de {:.2f}.'.format(imc))
elif 30 < imc <= 40:
    print('Obesidade com IMC de {:.2f}.'.format(imc))
elif imc > 40:
    print('Obesidade mórbida com IMC de {:.2f}.'.format(imc))