Nome = str(input("Nome: "))
Peso = float(input("Peso: "))

print("Nome fornecido:", Nome)
print(f"Peso fornecido: {Peso}")

if Peso < 65:
    Categoria = "Pena"
elif Peso >= 65 and Peso < 72:
    Categoria = "Leve"
elif Peso >= 72 and Peso < 79:
    Categoria = "Ligeiro"
elif Peso >= 79 and Peso < 86:
    Categoria = "Meio Médio"
elif Peso >= 86 and Peso < 93:
    Categoria = "Médio"
elif Peso >= 93 and Peso < 100:
    Categoria = "Meio Pesado"
else:
    Categoria = "Pesado"

print(f"O lutador {Nome} pesa {Peso} e se enquadra na categoria {Categoria}")