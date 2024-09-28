"""
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, calculando a
soma de todos os valores digitados.

"""

N = int(input("Quantidade Numeros: "))
Soma = 0
Cont = 0
i = 1

while Cont < N:
    R = float(input(f"Real {i}: "))
    Soma = Soma + R
    i = i + 1
    Cont = Cont + 1

print(f"Soma Numeros Reais: {Soma}")
