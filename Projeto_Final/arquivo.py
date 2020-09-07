from menu import cabecalho
def abrir_arquivo (nome):
    try:
        a = open(nome,'r')
        a.close()
        print('Arquivo aberto com sucesso')
    except:
        criar_arquivo(nome)

def criar_arquivo (nome):
    try:
        a = open(nome, 'w+')
        a.close()
        print('Arquivo criado com sucesso.')
    except:
        print('Erro na criação do arquivo.')

def ler_arquivo (nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        for linha in a:
            dado = linha.split(';')
            print(f'{dado[0]:<30}{dado[1]:>15} anos')
    finally:
        a.close()

#Aqui eu cadastro uma nova pessoa
def cadastrar (nome, pessoa='Desconhecido', idade='0' ):
    cabecalho('Novo Cadastro')
    pessoa = input('Nome: ')
    idade = int(input('Idade: '))
    try:
        a = open(nome,'a')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{pessoa};{idade};\n')
        except:
            print('Erro no cadastro')
        finally:
            print(f'Novo Registro de {pessoa} adicionado.')
