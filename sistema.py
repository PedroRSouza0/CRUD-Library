from time import sleep


def titulo(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30) 


def menu():
    while True:
        try:
            titulo('CRUD BIBLIOTECA')
            print('1 - Cadastrar Livro ')
            print('2 - Cadastrar Cliente ')
            print('3 - Vizualizar dados')
            print('4 - Sair')

            escolha = int(input('>>> '))
            if escolha in [1, 2, 3, 4]:
                return escolha
            else: 
                print('\nDigite um valor válido.')
        except (ValueError, TypeError):
            print('\nERRO. Digite uma opção válida')
        except KeyboardInterrupt:
            print('\nO usuário encerrou pelo teclado')
            return 4
        
        

def saida():
    print('-' * 30)
    print('Encerrando...'.center(30))
    sleep(0.7)
    print('-' * 30)