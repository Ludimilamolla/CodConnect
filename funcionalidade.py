from tkinter import messagebox
from database import *

# Funçao - Fazer upload de um currículo em PDF
def fazer_upload_curriculo():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with open(file_path, 'rb') as file:
            return file.read()
    return None

# Funçao - Criar o perfil do candidato
def criar_perfil_desenvolvedor():
    nome = nome_entry.get()
    email = email_entry.get()
    experiencia = experiencia_text.get("1.0", "end")
    curriculo = fazer_upload_curriculo()

    if nome and email and experiencia and curriculo:
        candidato_id = adicionar_candidato(nome, email, experiencia, curriculo)
        messagebox.showinfo("Sucesso", f"Perfil criado com sucesso (ID: {candidato_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos e faça upload do currículo em PDF")

# Funçao - Criar o perfil do recrutador
def criar_perfil_recrutador():
    nome = nome_entry.get()
    empresa = empresa_entry.get()
    email = email_entry.get()
    
    if nome and empresa and email:
        recrutador_id = adicionar_recrutador(nome, empresa, email)
        messagebox.showinfo("Sucesso", f"Perfil de Recrutador criado com sucesso (ID: {recrutador_id})")
    else:
        messagebox.showerror("Erro", "Preencha todos os campos")

# Funçao - Criar uma vaga
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