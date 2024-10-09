"""
Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida o
programa deve juntar as duas listas em uma única lista com o tamanho 20.
"""

Tamanho = 10
LA = []
LB = []

i = 0
print("\nLista 1:")
while i < Tamanho:
        Valor = int(input(f"    Valor {i+1}: "))
        LA.append(Valor)
        i += 1

print("\nLista 2:")
i = 0
while i < Tamanho:
    Valor = int(input(f"    Valor {i+1}: "))
    LB.append(Valor)
    i += 1

Lista = LA + LB

print(f"Sua lista:\n{Lista}")
print("\nFim do Programa")