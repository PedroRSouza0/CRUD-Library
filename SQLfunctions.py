from script import cursor, conexao
from Entities.Classes.Livro import Livro 
from Entities.Classes.Cliente import Cliente
import os

def cadastrar_livro(livro):
    try:
        cursor.execute(f"""INSERT INTO livro(titulo, autor, editora)
                    VALUES (?, ?, ?)""",(livro.titulo, livro.autor, livro.editora))
        conexao.commit()
    except Exception as erro:
        print(f'ERRO ao cadastrar um novo livro: {erro}')
        return False
    except (ValueError, TypeError):
        print(f'ERRO ao cadastrar um novo livro: {erro}')
        return False
    else:
        os.system('cls')
        print('Livro cadastrado com sucesso!')
        return True


def cadastrar_cliente(cliente):
    try:
        cursor.execute(f"""INSERT INTO cliente (nome, ano_nascimento, email) 
                    VALUES(?, ?, ?)""", (cliente.nome, cliente.ano_nascimento, cliente.email))
        conexao.commit()
    except Exception as erro:
        print(f'ERRO ao cadastrar um novo cliente: {erro}')
        return False
    except (ValueError, TypeError):
        print(f'ERRO ao cadastrar um novo livro: {erro}')
        return False
    else:
        os.system('cls')
        print(f'Novo cliente cadastrado com sucesso!')
        return True



def select(field, table, where=''):
    """
    :param: field: Campo a ser mostrado
    :param: table: Tabela
    """
    if where.isnumeric():
        cursor.execute(f"""SELECT {field} FROM {table} WHERE id_cliente={where}""")
    else:
        cursor.execute(f"""SELECT {field} FROM {table}""")
    retorno = cursor.fetchall()
    return retorno
