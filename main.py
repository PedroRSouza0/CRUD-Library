import script
from CRUD import *
from time import sleep
from Entities.Classes.Livro import Livro 
from Entities.Classes.Cliente import Cliente
import sistema as sys
import os

while True:

    escolha = sys.menu()

    if escolha == 1:
        while True:
            titulo = str(input('Titulo: '))
            autor = str(input('Autor: '))
            editora = str(input('Editora: '))

            livro = Livro(titulo, autor, editora)
            controle = cadastrar_livro(livro)  # Cadastra e controle recebe valor

            if controle:
                break

    elif escolha == 2:
        while True:
            c = False
            while not c:
                try:
                    nome = str(input('Nome: '))
                    ano_nascimento = int(input('Ano de nascimento: '))
                    e_mail = str(input('E-mail: '))
                except (ValueError, TypeError):
                    print('ERRO. Digite um valor váido')
                except KeyboardInterrupt:
                    print('O usuário finalizou pelo teclado')
                    c = True
                except Exception as erro:
                    print(f'ERRO. {erro}')
                else:
                    c = True

            cliente = Cliente(nome, ano_nascimento, e_mail)
            controle = cadastrar_cliente(cliente) # cadastra e controle recebe valor

            if controle:
                res = str(input('Deseja cadastrat outro? [Y/N] ')).upper()[0]
                while res not in ['Y' , 'N']:
                    print('Digite uma opção válida!')
                    res = str(input('Deseja continuar? [Y/N] ')).upper()[0]
            if res.upper() == 'N':
                break
           
    elif escolha == 3:
        
        sys.verDadosPrint()
        try:
            opcao = str(input('>>> '))
        except Exception as erro:
            print(f'ERRO: {erro}')
        
        if opcao == '1':
            ver_livros(opcao)
            sleep(1)
        elif opcao == '2':
            ver_cliente(opcao)        
            sleep(1)


    elif escolha == 4:
        sys.saida()
        break
    