a = 'base_dados.txt'
# Abrir ou criar arquivo
from arquivo import *
abrir_arquivo(a)
from menu import *
# Menu Principal
opcoes()
# Escolha da opção:
o = validar('\033[32mSua opção:\033[m ')
while o != 3:
    if o == 1:
        ler_arquivo(a)
        opcoes()
        o = validar('\033[32mSua opção:\033[m ')
    elif o == 2:
        cadastrar(a)
        opcoes()
        o = validar('\033[32mSua opção:\033[m ')
cabecalho("Saindo do sistema... Até Logo!")