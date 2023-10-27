import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from database import *


# Funçao - Fazer upload de um currículo em PDF
def fazer_upload_curriculo():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with open(file_path, 'rb') as file:
            return file.read()
    return None

# Função - Criar o perfil do desenvolvedor

def criar_perfil_desenvolvedor():
    global nome_entry, email_entry, experiencia_text
    nome = nome_entry.get()
    email = email_entry.get()
    experiencia = experiencia_text.get("1.0", "end")
    curriculo = fazer_upload_curriculo()
    if nome and email and experiencia and curriculo:
        desenvolvedor_id = adicionar_desenvolvedor(nome, email, experiencia, curriculo)
        messagebox.showinfo("Sucesso", f"Perfil criado com sucesso (ID: {desenvolvedor_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos e faça upload do currículo em PDF")

# Função - Criar o perfil do recrutador
def criar_perfil_recrutador():
    nome = nome_entry.get()
    empresa = empresa_entry.get()
    email = email_entry.get()
    
    if nome and empresa and email:
        recrutador_id = adicionar_recrutador(nome, empresa, email)
        messagebox.showinfo("Sucesso", f"Perfil de Recrutador criado com sucesso (ID: {recrutador_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos")

# Função - Criar uma vaga
def criar_vaga():
    titulo = titulo_entry.get()
    descricao = descricao_text.get("1.0", "end")
    empresa = empresa_entry.get()
    salario = salario_entry.get()
    requisitos = requisitos_text.get("1.0", "end")
    
    try:
        salario = float(salario)
    except ValueError:
        salario = 0.0

    if titulo and descricao and empresa and salario >= 0 and requisitos:
        vaga_id = adicionar_vaga(titulo, descricao, empresa, salario, requisitos)
        messagebox.showinfo("Sucesso", f"Vaga criada com sucesso (ID: {vaga_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente")

# Funçao - Listar candidatos do banco de dados
def desenvolvedores():
    cursor.execute("SELECT ID_cand, Nome FROM Desenvolvedor")
    desenvolvedores = cursor.fetchall()
    return desenvolvedores

# Funçao - Listar recrutador do banco de dados
def listar_recrutador():
    cursor.execute("SELECT ID_rec, Nome, empresa FROM Candidato")
    recrutadores = cursor.fetchall()
    return recrutadores

# Funçao - Listar vagas do banco de dados
def listar_vagas():
    cursor.execute("SELECT ID_vaga, Titulo FROM Vagas")
    vagas = cursor.fetchall()
    return vagas

# Função - Exibir a lista de desenvolvedores em um Listbox
def exibir_lista_desenvolvedores():
    desenvolvedores = listar_desenvolvedores()
    listbox.delete(0, tk.END)  # Limpa a lista existente
    for desenvolvedor in desenvolvedores:
        listbox.insert(tk.END, f"{desenvolvedor[0]} - {desenvolvedor[1]}")

# Função - Exibir a lista de recrutadores em um Listbox
def exibir_lista_recrutadores():
    recrutadores = listar_recrutadores()
    listbox.delete(0, tk.END)  # Limpa a lista existente
    for recrutador in recrutadores:
        listbox.insert(tk.END, f"{recrutador[0]} - {recrutador[1]}")

# Função - Exibir a lista de vagas em um Listbox
def exibir_lista_vagas():
    vagas = listar_vagas()
    listbox.delete(0, tk.END)  # Limpa a lista existente
    for vaga in vagas:
        listbox.insert(tk.END, f"{vaga[0]} - {vaga[1]}")

# Função - Validar email
def validar_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return False
    return True

# Função - Exibir detalhes dos registros de desenvolvedor
def exibir_detalhes_desenvolvedor(index):
    desenvolvedores = listar_desenvolvedores()
    if 0 <= index < len(desenvolvedores):
        detalhes = desenvolvedores[index]

        # Função - Exibir detalhes dos registros de desenvolvedor
        mensagem = f"Detalhes do Desenvolvedor\n\n"
        mensagem += f"Nome: {detalhes_desenvolvedor[1]}\n"
        mensagem += f"E-mail: {detalhes_desenvolvedor[2]}\n"
        mensagem += f"Experiência: {detalhes_desenvolvedor[3]}\n"
        
        # Cria uma mensagem com os detalhes do desenvolvedor
        messagebox.showinfo("Detalhes do Desenvolvedor", mensagem)

# Função - Exibir detalhes dos registros de recrutador
def exibir_detalhes_recrutador(index):
    recrutadores = listar_recrutadores()
    if 0 <= index < len(recrutadores):
        detalhes = recrutadores[index]

        # Cria uma mensagem com os detalhes do recrutador
        mensagem = f"Detalhes do Recrutador\n\n"
        mensagem += f"Nome: {detalhes_recrutador[1]}\n"
        mensagem += f"Empresa: {detalhes_recrutador[2]}\n"
        mensagem += f"E-mail: {detalhes_recrutador[3]}\n"
        
        # Cria uma mensagem com os detalhes do recrutador
        messagebox.showinfo("Detalhes do Recrutador", mensagem)


# Função - Exibir detalhes dos registros de vaga
def exibir_detalhes_vaga(index):
    vagas = listar_vagas()
    if 0 <= index < len(vagas):
        detalhes = vagas[index]

        # Cria uma mensagem com os detalhes da vaga
        mensagem = f"Detalhes da Vaga\n\n"
        mensagem += f"Título: {detalhes_vaga[1]}\n"
        mensagem += f"Descrição: {detalhes_vaga[2]}\n"
        mensagem += f"Empresa: {detalhes_vaga[3]}\n"
        mensagem += f"Salário: R$ {detalhes_vaga[4]:.2f}\n"
        mensagem += f"Requisitos: {detalhes_vaga[5]}\n"

        # Exibe a mensagem em uma janela de pop-up
        messagebox.showinfo("Detalhes da Vaga", mensagem)

