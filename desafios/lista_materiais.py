itens = {}

#x = list(map(str, input("Enter multiple values: ").split()))

for i in range(3):
    itens[i] = input("Digite: ")

print(itens)
# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {itens[item]}")