"""
Escreva um programa que leia valores numéricos inteiros e totalize (totalizar é somar todos os números)
separadamente os positivos e os negativos até que o usuário digite 0. Ao final mostre na tela esses dois
totais.
"""

S_Positivos = 0
S_Negativos = 0
N = int(input("N:"))

while N != 0:
    if N < 0:
        S_Negativos = S_Negativos + N
    else:
        S_Positivos = S_Positivos + N
    N = int(input("N:"))

print(f"Total dos positivos = {S_Positivos}")
print(f"Total dos Negativos = {S_Negativos}")