import tkinter as tk
from funcionalidade import *

# Funçao - Abrir a interface do candidato
def abrir_interface_desenvolvedor():
    desenvolvedor_window = tk.Toplevel(root)
    desenvolvedor_window.title("DEVConnect - Desenvolvedor")

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
