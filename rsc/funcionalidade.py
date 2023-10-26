from database import *

def criar_perfil_candidato(nome, email, experiencia, curriculo):
    conn, cursor = conectar_banco_dados()
    candidato_id = adicionar_candidato(conn, cursor, nome, email, experiencia, curriculo)
    conn.close()
    return candidato_id

# Outras funções para criar perfil de recrutador, criar vagas, listar candidatos, listar vagas, etc.
