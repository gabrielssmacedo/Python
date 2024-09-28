Salario = float(input())

if Salario > 0 and Salario <= 400.00:
    Novo_Salario = Salario * 1.15
    Reajuste = Novo_Salario - Salario
    Percentual = round((Reajuste * 100) / Salario)
elif Salario >= 400.01 and Salario <= 800.00:
    Novo_Salario = Salario * 1.12
    Reajuste = Novo_Salario - Salario
    Percentual = round((Reajuste * 100) / Salario)
elif Salario >= 800.01 and Salario <= 1200.00:
    Novo_Salario = Salario * 1.10
    Reajuste = Novo_Salario - Salario
    Percentual = round((Reajuste * 100) / Salario)
elif Salario >= 1200.01 and Salario <= 2000.00:
    Novo_Salario = Salario * 1.07
    Reajuste = Novo_Salario - Salario
    Percentual = round((Reajuste * 100) / Salario)
elif Salario > 2000.00:
    Novo_Salario = Salario * 1.04
    Reajuste = Novo_Salario - Salario
    Percentual = round((Reajuste * 100) / Salario)

print(f"Novo salario: {Novo_Salario:.2f}")
print(f"Reajuste ganho: {Reajuste:.2f}")
print(f"Em percentual: {Percentual} %")