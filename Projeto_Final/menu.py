#Formatação do cabeçalho
def cabecalho (txt):
    print('-' * 50)
    print(f'{txt:^50}')
    print('-' * 50)

#Aqui eu exibo as opções disponíveis
def opcoes ():
    cabecalho('MENU PRINCIPAL')
    print('\033[33m1 -\033[36m Ver pessoas cadastradas\033[m')
    print('\033[33m2 -\033[36m Cadastrar nova pessoa\033[m')
    print('\033[33m3 -\033[36m Sair do sistema\033[m')
    print('-' * 50)

#Aqui eu valido as opções que foram digitadas
def validar (txt):
    while True:
        try:
            n = int(input(txt))
        except:
            print('\033[31mErro, digite um número inteiro. \033[m')
            continue
        else:
            if n not in [1,2,3]:
                print('\033[31mErro, digite uma opção válida. \033[m')
                opcoes()
            else:
                return n
