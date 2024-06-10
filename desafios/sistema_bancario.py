import tkinter as tk
from tkinter import messagebox

# Constantes
LIMITE_SAQUES = 3
LIMITE = 500

# Variáveis Globais
saldo = 0
extrato = ""
numero_saques = 0

# Funções
def depositar():
    global saldo, extrato
    try:
        valor = float(entry_valor.get())
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Operação falhou! O valor informado é inválido.")
    except ValueError:
        messagebox.showerror("Erro", "Operação falhou! Valor inválido.")
    finally:
        entry_valor.delete(0, tk.END)

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

def exibir_extrato():
    global saldo, extrato
    extrato_text = "Não foram realizadas movimentações." if not extrato else extrato
    extrato_text += f"\nSaldo: R$ {saldo:.2f}"
    messagebox.showinfo("Extrato", extrato_text)

# Interface Gráfica
root = tk.Tk()
root.title("Sistema Bancário")

frame = tk.Frame(root)
frame.pack(pady=10)

label_valor = tk.Label(frame, text="Valor:")
label_valor.grid(row=0, column=0, padx=5, pady=5)
entry_valor = tk.Entry(frame)
entry_valor.grid(row=0, column=1, padx=5, pady=5)

button_depositar = tk.Button(frame, text="Depositar", command=depositar)
button_depositar.grid(row=1, column=0, padx=5, pady=5)

button_sacar = tk.Button(frame, text="Sacar", command=sacar)
button_sacar.grid(row=1, column=1, padx=5, pady=5)

button_extrato = tk.Button(frame, text="Extrato", command=exibir_extrato)
button_extrato.grid(row=2, column=0, columnspan=2, pady=5)

root.mainloop()
