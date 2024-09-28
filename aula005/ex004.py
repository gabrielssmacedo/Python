"""
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, calculando a
soma de todos os valores positivos fornecidos, ignorando os negativos
"""

N = int(input("Quantidade Numeros: "))
Soma = 0
Cont = 0
i = 1

while Cont < N:
    R = float(input(f"Real {i}: "))
    if R > 0:
        Soma = Soma + R
        Cont = Cont + 1
        i = i + 1
    else:
        Cont = Cont + 1
        i = i + 1

print(f"Soma Positivos: {Soma}")