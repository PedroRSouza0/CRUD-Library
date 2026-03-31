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


def ver_livros(campos='*', condicao=0):
    """
    SELECT <campos> FROM <tabela> WHERE <condicao>
    """
    try:
        if not condicao:
            query = f"SELECT {campos} FROM livro"
            cursor.execute(query)
            saida = cursor.fetchall() # Recebe a query
            for linha in saida:
                print(linha)
        elif condicao:
            try:
                query = f"SELECT {campos} FROM livro WHERE id_livro=10"
                cursor.execute(query)
                saida = cursor.fetchall()
                print(saida)
            except Exception as erro:
                print(f'ERRO. {erro}')
    except Exception as erro:
        print(f'ERRO ao consultar livros, {erro}')
    

def ver_cliente(campos, condicao=0):
    try:
        if not condicao:
            query = f"SELECT {campos} FROM cliente"
            cursor.execute(query)
            saida = cursor.fetchall()
            for linha in saida:
                print(linha)
    except Exception as erro:
        print(f'ERRO ao consultar clientes, {erro}')