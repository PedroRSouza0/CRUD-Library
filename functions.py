from script import cursor, conexao

def cadastrar_livro(livro):
    cursor.execute(f"""INSERT INTO livro(titulo, autor, editora)
                   VALUES ('{livro[0]}', '{livro[1]}', '{livro[2]}')""")
    conexao.commit()
    return False


def cadastrar_cliente(nome, ano, email):
    cursor.execute(f"""INSERT INTO cliente (nome, ano_nascimento, email) 
                   VALUES('{nome}', {ano}, '{email}')""")
    conexao.commit()
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
