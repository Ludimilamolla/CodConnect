import tkinter as tk
from funcionalidade import *
root = tk.Tk()

# Funçao - Abrir a interface do candidato
def abrir_interface_desenvolvedor():
    desenvolvedor_window = tk.Toplevel(root)
    desenvolvedor_window.title("CodConnect - Desenvolvedor")

    # Labels e campos de entrada
    tk.Label(desenvolvedor_window, text="Nome:").pack()
    global nome_entry
    nome_entry = tk.Entry(desenvolvedor_window)
    nome_entry.pack()

    tk.Label(desenvolvedor_window, text="E-mail:").pack()
    global email_entry
    email_entry = tk.Entry(desenvolvedor_window)
    email_entry.pack()

    tk.Label(desenvolvedor_window, text="Experiência:").pack()
    global experiencia_text
    experiencia_text = tk.Text(desenvolvedor_window, height=5, width=40)
    experiencia_text.pack()

    # Botão - Fazer upload de currículo
    upload_button = tk.Button(desenvolvedor_window, text="Fazer Upload de Currículo (PDF)", command=fazer_upload_curriculo)
    upload_button.pack(padx=15, pady=15)

    # Botão - Criar o perfil do desenvolvedor
    criar_perfil_button = tk.Button(desenvolvedor_window, text="Criar Perfil de Desenvolvedor", command=criar_perfil_desenvolvedor)
    criar_perfil_button.pack(padx=15, pady=15)

    # Botão - Listar vagas
    listar_vagas_button = tk.Button(desenvolvedor_window, text="Listar Vagas", command=exibir_lista_vagas)
    listar_vagas_button.pack(padx=15, pady=15)

    # Botão - Fechar a janela do desenvolvedor
    fechar_button = tk.Button(desenvolvedor_window, text="Fechar", command=desenvolvedor_window.destroy)
    fechar_button.pack(padx=15, pady=15)

def chamar_criar_perfil():
    print("Nome Entry:", nome_entry.get())
    print("Email Entry:", email_entry.get())
    print("Experiência Text:", experiencia_text.get("1.0", "end"))
        
    criar_perfil_desenvolvedor(nome_entry, email_entry, experiencia_text)

# Funçao - Abrir a interface do recrutador
def abrir_interface_recrutador():
    recrutador_window = tk.Toplevel(root)
    recrutador_window.title("CodConnect - Recrutador")

    # Labels e campos de entrada
    tk.Label(recrutador_window, text="Nome:").pack()
    global nome_entry
    nome_entry = tk.Entry(recrutador_window)
    nome_entry.pack()

    tk.Label(recrutador_window, text="Empresa:").pack()
    global empresa_entry
    empresa_entry = tk.Entry(recrutador_window)
    empresa_entry.pack()

    tk.Label(recrutador_window, text="email:").pack()
    global email_entry
    email_entry = tk.Entry(recrutador_window)
    email_entry.pack()

    # Botão - Criar o perfil do recrutador
    criar_perfil_button = tk.Button(recrutador_window, text="Criar Perfil de Recrutador", command=criar_perfil_recrutador)
    criar_perfil_button.pack(padx=15, pady=15)

    # Botão - Listar vagas
    listar_vagas_button = tk.Button(recrutador_window, text="Listar Vagas", command=exibir_lista_vagas)
    listar_vagas_button.pack(padx=15, pady=15)

    # Botão - Listar candidatos
    listar_candidatos_button = tk.Button(recrutador_window, text="Listar Candidatos", command=exibir_lista_candidatos)
    listar_candidatos_button.pack(padx=15, pady=15)

     # Botão - Fechar a janela do recrutador
    fechar_button = tk.Button(recrutador_window, text="Fechar", command=recrutador_window.destroy)
    fechar_button.pack(padx=15, pady=15)

# Funçao - Abrir a interface de vagas
def abrir_interface_vagas():
    vagas_window = tk.Toplevel(root)
    vagas_window.title("CodConnect - Vagas")

    # Labels e campos de entrada
    tk.Label(vagas_window, text="Título da Vaga:").pack()
    global titulo_entry
    titulo_entry = tk.Entry(vagas_window)
    titulo_entry.pack()

    tk.Label(vagas_window, text="Descrição da Vaga:").pack()
    global descricao_text
    descricao_text = tk.Text(vagas_window, height=5, width=40)
    descricao_text.pack()

    tk.Label(vagas_window, text="Empresa:").pack()
    global empresa_entry
    empresa_entry = tk.Entry(vagas_window)
    empresa_entry.pack()

    tk.Label(vagas_window, text="Salário:").pack()
    global salario_entry
    salario_entry = tk.Entry(vagas_window)
    salario_entry.pack()

    tk.Label(vagas_window, text="Requisitos:").pack()
    global requisitos_text
    requisitos_text = tk.Text(vagas_window, height=5, width=40)
    requisitos_text.pack()

    # Botão - Criar uma vaga
    criar_vaga_button = tk.Button(vagas_window, text="Criar Vaga", command=criar_vaga)
    criar_vaga_button.pack(padx=15, pady=15)

    # Botão - Listar vagas
    listar_vagas_button = tk.Button(vagas_window, text="Listar Vagas", command=exibir_lista_vagas)
    listar_vagas_button.pack(padx=15, pady=15)

    # Botão - Fechar a janela de vagas
    fechar_button = tk.Button(vagas_window, text="Fechar", command=vagas_window.destroy)
    fechar_button.pack(padx=15, pady=15)

    # Lista de vagas e candidatos
    global listbox
    listbox = tk.Listbox(vagas_window, selectmode=tk.SINGLE, width=60, height=15)
    listbox.pack(padx=15, pady=15)

# Funçao - Fechar a janela do desenvolvedor
def fechar_janela_desenvolvedor():
    desenvolvedor_window.destroy()

# Funçao - Fechar a janela de vagas
def fechar_janela_vagas():
    vagas_window.destroy()

# Funçao - Listar candidatos no Listbox
def exibir_lista_candidatos():
    candidato_window = tk.Toplevel(root)
    candidato_window.title("Lista de Candidatos")

    # Lista de candidatos
    listbox = tk.Listbox(candidato_window, selectmode=tk.SINGLE, width=60, height=15)
    listbox.pack()

    candidatos = listar_candidatos()
    for candidato in candidatos:
        listbox.insert(tk.END, f"{candidato[0]} - {candidato[1]}")

# Funçao - Listar vagas no Listbox
def exibir_lista_vagas():
    vagas_window = tk.Toplevel(root)
    vagas_window.title("Lista de Vagas")

    # Lista de vagas
    listbox = tk.Listbox(vagas_window, selectmode=tk.SINGLE, width=60, height=15)
    listbox.pack()

    vagas = listar_vagas()
    for vaga in vagas:
        listbox.insert(tk.END, f"{vaga[0]} - {vaga[1]}")

# Interface principal
root = tk.Tk()
root.title("CodConnect")

# Botões - Acessar as interfaces
desenvolvedor_button = tk.Button(root, text="Desenvolvedor", command=abrir_interface_desenvolvedor)
recrutador_button = tk.Button(root, text="Recrutador", command=abrir_interface_recrutador)
vagas_button = tk.Button(root, text="Vagas", command=abrir_interface_vagas)


desenvolvedor_button.pack(padx=15, pady=15)
recrutador_button.pack(padx=15, pady=15)
vagas_button.pack(padx=15, pady=15)

root.mainloop()

# Fechar a conexão com o banco de dados
conn.close()