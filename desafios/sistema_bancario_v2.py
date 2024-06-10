import tkinter as tk
from tkinter import messagebox
import os

# Constantes
LIMITE_SAQUES = 3
LIMITE = 500

# Variáveis Globais
saldo = 0
extrato = ""
numero_saques = 0
usuarios = {}
current_user = None

# Funções de Usuário
def carregar_usuarios():
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as file:
            for line in file:
                nome, cpf, nascimento, endereco, senha = line.strip().split(";")
                usuarios[cpf] = {"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco, "senha": senha}

def salvar_usuario(nome, cpf, nascimento, endereco, senha):
    with open("usuarios.txt", "a") as file:
        file.write(f"{nome};{cpf};{nascimento};{endereco};{senha}\n")
    usuarios[cpf] = {"nome": nome, "cpf": cpf, "nascimento": nascimento, "endereco": endereco, "senha": senha}

def criar_usuario():
    def salvar_novo_usuario():
        nome = entry_nome.get()
        cpf = entry_cpf.get()
        nascimento = entry_nascimento.get()
        endereco = entry_endereco.get()
        senha = entry_senha.get()
        confirmar_senha = entry_confirmar_senha.get()
        
        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        if cpf in usuarios:
            messagebox.showerror("Erro", "CPF já cadastrado.")
            return

        salvar_usuario(nome, cpf, nascimento, endereco, senha)
        messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
        criar_usuario_window.destroy()

    criar_usuario_window = tk.Toplevel(root)
    criar_usuario_window.title("Criar Usuário")

    tk.Label(criar_usuario_window, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = tk.Entry(criar_usuario_window)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(criar_usuario_window, text="CPF:").grid(row=1, column=0, padx=5, pady=5)
    entry_cpf = tk.Entry(criar_usuario_window)
    entry_cpf.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(criar_usuario_window, text="Data de Nascimento:").grid(row=2, column=0, padx=5, pady=5)
    entry_nascimento = tk.Entry(criar_usuario_window)
    entry_nascimento.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(criar_usuario_window, text="Endereço:").grid(row=3, column=0, padx=5, pady=5)
    entry_endereco = tk.Entry(criar_usuario_window)
    entry_endereco.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(criar_usuario_window, text="Senha:").grid(row=4, column=0, padx=5, pady=5)
    entry_senha = tk.Entry(criar_usuario_window, show="*")
    entry_senha.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(criar_usuario_window, text="Confirmar Senha:").grid(row=5, column=0, padx=5, pady=5)
    entry_confirmar_senha = tk.Entry(criar_usuario_window, show="*")
    entry_confirmar_senha.grid(row=5, column=1, padx=5, pady=5)

    tk.Button(criar_usuario_window, text="Salvar", command=salvar_novo_usuario).grid(row=6, column=0, columnspan=2, pady=5)

def login():
    global current_user

    cpf = entry_cpf_login.get()
    senha = entry_senha_login.get()

    if cpf in usuarios and usuarios[cpf]["senha"] == senha:
        current_user = usuarios[cpf]
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        login_window.destroy()
        exibir_menu_principal()
    else:
        messagebox.showerror("Erro", "CPF ou senha inválidos.")

def exibir_tela_login():
    global login_window, entry_cpf_login, entry_senha_login
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    tk.Label(login_window, text="CPF:").grid(row=0, column=0, padx=5, pady=5)
    entry_cpf_login = tk.Entry(login_window)
    entry_cpf_login.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(login_window, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
    entry_senha_login = tk.Entry(login_window, show="*")
    entry_senha_login.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(login_window, text="Entrar", command=login).grid(row=2, column=0, columnspan=2, pady=5)
    tk.Button(login_window, text="Criar Usuário", command=criar_usuario).grid(row=3, column=0, columnspan=2, pady=5)

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")

def sacar():
    global saldo, extrato, numero_saques
    try:
        valor = float(entry_valor.get())

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            messagebox.showerror("Erro", "Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            messagebox.showerror("Erro", "Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            messagebox.showerror("Erro", "Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")
    except ValueError:
        messagebox.showerror("Erro", "Operação falhou! Valor inválido.")
    finally:
        entry_valor.delete(0, tk.END)

def exibir_extrato(*args):
    global saldo, extrato
    extrato_text = "Não foram realizadas movimentações." if not extrato else extrato
    extrato_text += f"\nSaldo: R$ {saldo:.2f}"
    messagebox.showinfo("Extrato", extrato_text)

def exibir_menu_principal():
    global entry_valor
    frame = tk.Frame(root)
    frame.pack(pady=10)

    label_valor = tk.Label(frame, text="Valor:")
    label_valor.grid(row=0, column=0, padx=5, pady=5)
    entry_valor = tk.Entry(frame)
    entry_valor.grid(row=0, column=1, padx=5, pady=5)

    button_depositar = tk.Button(frame, text="Depositar", command=lambda: depositar(float(entry_valor.get())))
    button_depositar.grid(row=1, column=0, padx=5, pady=5)

    button_sacar = tk.Button(frame, text="Sacar", command=sacar)
    button_sacar.grid(row=1, column=1, padx=5, pady=5)

    button_extrato = tk.Button(frame, text="Extrato", command=lambda: exibir_extrato(saldo, extrato))
    button_extrato.grid(row=2, column=0, columnspan=2, pady=5)

# Interface Gráfica
root = tk.Tk()
root.title("Sistema Bancário")

carregar_usuarios()

button_login = tk.Button(root, text="Entrar", command=exibir_tela_login)
button_login.pack(pady=10)

root.mainloop()
