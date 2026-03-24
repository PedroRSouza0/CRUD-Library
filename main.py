import script
from functions import *
from time import sleep
while True:
    print('\n1 - Cadastrar Livro ')
    print('2 - Cadastrar Cliente ')
    print('3 - Vizualizar dados')
    print('4 - Sair')

    escolha = int(input('>>> '))
    if escolha == 1:
        while True:
            livro = []
            titulo = str(input('Titulo: '))
            autor = str(input('Autor: '))
            editora = str(input('Editora: '))

            livro.append(titulo)
            livro.append(autor)
            livro.append(editora)

            controle = cadastrar_livro(livro)
            if not controle:
                break
    if escolha == 2:
        while True:

            nome = str(input('Nome: '))
            ano_nascimento = int(input('Ano de nascimento: '))
            e_mail = str(input('E-mail: '))
            controle = cadastrar_cliente(nome, ano_nascimento, e_mail)

            if controle:
                print('\nCliente Cadastrado com sucesso!')
            
            res = str(input('Deseja continuar? [Y/N] ')).upper()[0]
            while res not in ['Y' , 'N']:
                print('Digite uma opção válida!')
                res = str(input('Deseja continuar? [Y/N] ')).upper()[0]
            if res.upper() == 'N':
                break
    
    if escolha == 3:
        while True:
            for re in select('*', 'livro'):
                print(re)
            break

    if escolha == 4:
        print('Encerrando...')
        sleep(1.2)
        break


            
