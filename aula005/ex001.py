"""
Escreva um programa que calcule os N primeiros termos de uma progressão geométrica (PG) com razão
R e primeiro termo P fornecidos pelo usuário. Também deve ser calculada e apresentada a soma desses
N termos
"""

N = int(input("Quantidade de Termos:"))
P = int(input("Primeiro Termo:"))
R = int(input("Razão Geométrica:"))
i = 0
Soma = 0

while i < N:
    print(P)
    Soma = Soma + P
    P = P * R
    i = i + 1

print(f"Soma Termos PG: {Soma}")