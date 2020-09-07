def maior(* num):
    a = max(* num)
    print(a)

resp = 'S'
a = []

while True:
    if resp in "Ss":
        b = int(input('Escreva um número - '))
        a.append(b)
        resp = input('Cadastrar outro número? - ').strip().upper()[0]
    else:
        break
maior(a)