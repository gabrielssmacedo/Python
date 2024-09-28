"""
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o
menor e o maior, apresentando-os na tela.
"""

N = int(input())
i = 0
V_anterior = 0

while i < N:
    V = float(input())
    if V > V_anterior:
        Maior = V
        Menor = V_anterior
    else:
        Maior = V_anterior
        Menor = V
    print(f"Maior: {Maior}")
    print(f"Menor: {Menor}")
    V_anterior = V
    i += 1
