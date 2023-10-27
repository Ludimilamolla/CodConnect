import sqlite3

# Funçao - Conectar ao banco de dados SQLite
def conectar_banco_dados():
    conn = sqlite3.connect('agencia.db')
    cursor = conn.cursor()
    return conn, cursor

# Funçao - Criar tabelas no banco de dados
def criar_tabelas(conn, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Desenvolvedor (
            ID_cand INTEGER PRIMARY KEY,
            Nome TEXT,
            E_mail TEXT,
            Experiencia TEXT,
            Curriculo BLOB
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Recrutador (
            ID_rec INTEGER PRIMARY KEY,
            Nome TEXT,
            Empresa TEXT,
            E_mail TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Vagas (
            ID_vaga INTEGER PRIMARY KEY,
            Titulo TEXT,
            Descricao TEXT,
            Empresa TEXT,
            Salario REAL,
            Requisitos TEXT
        )
    ''')

    conn.commit()

# Conectar ao banco de dados e criar tabelas
conn, cursor = conectar_banco_dados()
criar_tabelas(conn, cursor)

# Funçao - Adicionar um desenvolvedor ao banco de dados
def adicionar_desenvolvedor(nome, email, experiencia, curriculo):
    cursor.execute('INSERT INTO Desenvolvedor (Nome, E_mail, Experiencia, Curriculo) VALUES (?, ?, ?, ?)',
                   (nome, email, experiencia, curriculo))
    conn.commit()
    return cursor.lastrowid

# Funçao - Adicionar um recrutador ao banco de dados
def adicionar_recrutador(nome, empresa, email):
    cursor.execute('INSERT INTO Recrutador (Nome, Empresa, E_mail) VALUES (?, ?, ?)',
                   (nome, empresa, email))
    conn.commit()
    return cursor.lastrowid

# Funçao - Adicionar uma vaga ao banco de dados
def adicionar_vaga(titulo, descricao, empresa, salario, requisitos):
    cursor.execute('INSERT INTO Vagas (Titulo, Descricao, Empresa, Salario, Requisitos) VALUES (?, ?, ?, ?, ?)',
                   (titulo, descricao, empresa, salario, requisitos))
    conn.commit()
    return cursor.lastrowid

# Funçao - Listar candidatos do banco de dados
def listar_desenvolvedores():
    cursor.execute("SELECT ID_cand, Nome FROM Desenvolvedor")
    desenvolvedores = cursor.fetchall()
    return desenvolvedores

# Funçao - Listar recrutadores do banco de dados
def listar_recrutadores():
    cursor.execute("SELECT ID_rec, Nome, Empresa FROM Recrutador")
    recrutadores = cursor.fetchall()
    return recrutadores

# Funçao - Listar vagas do banco de dados
def listar_vagas():
    cursor.execute("SELECT ID_vaga, Titulo FROM Vagas")
    vagas = cursor.fetchall()
    return vagas

# Fechar a conexão com o banco de dados
conn.commit()