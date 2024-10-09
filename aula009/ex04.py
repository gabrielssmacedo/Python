"""
Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida preencha uma lista
com N elementos inteiros gerados aleatoriamente entre 0 e 1000
"""

from random import randint

Lista = []

N = int(input("Digite um número: "))
while N <= 0 or N >= 50:
    print("O número deve estar entre 0 e 50!")
    N = int(input("Digite um número: "))

i = 0
while i < N:
    Valor = randint(0, 1000)
    Lista.append(Valor)
    i += 1

print(f"\nSua lista:\n{Lista}")

print("\nFim do Programa")
