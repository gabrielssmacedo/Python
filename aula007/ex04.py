"""
Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida
o programa deve juntar as duas listas em uma única com o tamanho 20.
"""
L1 = []
L2 = []
i = 0
j = 0

print("Elementos Lista 1: ")
while i < 10:
    E = int(input(f"Elemento {i+1}: "))
    L1.append(E)
    i += 1

print("Elementos Lista 2: ")
while j < 10:
    E = int(input(f"Elemento {j+1}: "))
    L2.append(E)
    j += 1

k = p = 0
L3 = L1 + L2
Print = [L1, L2, L3]

for k in Print:
    print(f"\nL{p+1}: {k}")

print("\nFim do Programa")