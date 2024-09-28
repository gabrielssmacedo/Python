Salario = float(input())

if Salario > 0 and Salario <= 2000.00:
    print("Isento")
elif Salario >= 2000.01 and Salario <= 3000.00:
    Imposto = (Salario - 2000) * 0.08
    print(f"R$ {Imposto:.2f}")
elif Salario >= 3000.01 and Salario <= 4500.00:
    Imposto = 1000 * 0.08 + (Salario - 3000) * 0.18
    print(f"R$ {Imposto:.2f}")
elif Salario > 4500.00:
    Imposto = 1000 * 0.08 + 1500 * 0.18 + (Salario - 4500) * 0.28
    print(f"R$ {Imposto:.2f}")
else:
    print("Invalido")

