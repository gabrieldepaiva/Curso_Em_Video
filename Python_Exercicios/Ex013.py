salario = float(input('Qual o salário do funcionário? R$ '))
aumento = float(input('Qual a porcentagem de aumento de salário? '))/100
aumento2 = aumento*100
print("Um funcionário que ganhava R$ {}, com o aumento de {}%, passa a receber R$ {:.2f}.".format (salario, aumento2, salario * (1 + aumento)))