n = int(input('Digite um número entre de 0 a 20 - '))
e = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis',
     'Sete','Oito','Nove','Dez','Onze','Doze',
     'Treze','Quatorze','Quinze','Dezesseis','Dezessete',
     'Dezoito','Dezenove','Vinte')
while True:
    if n not in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
        n = int(input('Tente novamtente, digite um número inteiro de 0 a 20 - '))
    else:
        print(e[n])
        break
