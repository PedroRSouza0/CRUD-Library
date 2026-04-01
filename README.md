# 📚 CRUD Library

Sistema de gerenciamento de biblioteca desenvolvido em **Python** com integração ao banco de dados **SQLite**.

O objetivo do projeto é praticar **lógica de programação**, manipulação de dados e execução de **comandos SQL**, além de simular operações reais de um sistema de biblioteca.

---

## 🚀 Funcionalidades

- 📖 Cadastro de livros  
- 👤 Cadastro de clientes  
- 🔍 Consulta de registros  
- ✏️ Atualização de dados  
- ❌ Remoção de livros e clientes  

---

## 🛠️ Tecnologias utilizadas

- Python  
- SQLite (via biblioteca `sqlite3`)  

---

## 📂 Estrutura do Projeto
projeto/
│
├── controllers/
│ ├── init.py
│ └── CRUD.py
│
├── Entities/
│ ├── init.py
│ └── Classes/
│ ├── init.py
│ ├── Livro.py
│ └── Cliente.py
│
├── view/
│ ├── init.py
│ └── sistema.py
│
└── main.py

## ▶️ Como executar o projeto

⚠️ **Importante:**  
O projeto utiliza **imports relativos**, então ele deve ser executado corretamente para evitar erros.

### ✔️ Forma correta:

Execute o projeto a partir da raiz:

```bash
python main.py

