import sqlite3 as sql

# definir uma conexao
conexao = sql.connect("biblioteca.db")

# definir o cursor
cursor = conexao.cursor() # permite interagir com o banco através dos comandos SQL

# cria tabela livros
tabela_livros = """CREATE TABLE IF NOT EXISTS
    livro(id_livro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , titulo TEXT, autor TEXT, editora TEXT)"""

cursor.execute(tabela_livros)

tabela_cliente = """CREATE TABLE IF NOT EXISTS
    cliente(id_cliente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome TEXT NOT NULL, ano_nascimento INTEGER, email TEXT)"""

cursor.execute(tabela_cliente)
# tabela empréstimo
tabela_emprestimo = """CREATE TABLE IF NOT EXISTS
                emprestimo(id_livro INTEGER, id_cliente INTEGER, data_emprestimo DATETIME, FOREIGN KEY (id_livro) REFERENCES livro(id_livro), FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente))"""

cursor.execute(tabela_emprestimo)

#inserindo valores
# cursor.execute("""INSERT INTO livro(titulo, autor) 
#                 VALUES ('1983', 'George Orwell')""")

cursor.execute("""SELECT * FROM livro WHERE id_livro = 2""")
livros = cursor.fetchall() # traz o resultado da query e retorna numa lista. Ficar depois do select para retornar

# Delete
cursor.execute("DELETE FROM livro WHERE id_livro = 1")
# print(livros)

# for regis in livros:
#     id, titulo, autor, editora = regis
#     print(f"""Linha: {regis}
# ID {id}
# Titulo {titulo}
# Autor {autor}
# Editora {editora}""")
#     print()
conexao.commit() # para salvar 