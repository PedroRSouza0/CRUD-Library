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

            nome = str(input('Nome: '))
            ano_nascimento = int(input('Ano de nascimento: '))
            e_mail = str(input('E-mail: '))

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

        ver_livros('*', condicao=1)        
        break

    elif escolha == 4:
        sys.saida()
        break
    

            
