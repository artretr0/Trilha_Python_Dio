# Criando Dicionários
# Conjuntos não-ordenado de pares

pessoa = {"nome": "Arthur", "Idade": 22}

print(pessoa["nome"])


contatos = {
    "arthurcaldas99@gmail.com": {"Nome": "Arthur", "Telefone": "81 987302181"},
}

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# Métodos da classe dict

copia = contatos.copy()
copia.fromkeys(["nome", "telefone"], "none")
contatos.clear() #contatos = {}

print(copia)

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
print(carro.get("motor"))