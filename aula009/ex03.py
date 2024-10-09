"""
Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida leia N números reais
em uma lista A. Exiba a lista na tela, um elemento por linha.
"""
Lista = []

N = int(input("Números a serem lidos: "))
while N <= 0 or N >= 50:
    print("Número deve estar entre 0 e 50!")
    N = int(input("Números a serem lidos: "))

i = 0
while i < N:
    Valor = float(input(f" Valor {i+1}: "))
    Lista.append(Valor)
    i += 1

print("\nValores:")
k = 0
for k in Lista:
    print(k)
