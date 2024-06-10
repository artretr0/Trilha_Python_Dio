# Dominando Funções

def exibir_mensagem():
    print("Função que printa uma mensagem")

def nome_tela(nome = "Não Informado"):
    print(nome)

exibir_mensagem()

nome = input("Digite seu nome: ")
nome_tela(nome)

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com Sucesso! {marca}/{modelo}/{ano}/{placa}')

salvar_carro("Fiat", "Palio", 2020, "KJD-6121")

# *args -> recebe uma tupla
# **kwargs -> recebe um dicionário
