"""
Escreva um programa que contenha um laço que será executado enquanto o número digitado for
diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis
por 2 e por 3.
"""

i = 0
N = int(input())

while N != 0:
    if N % 2 == 0 and N % 3 == 0:
        print(f"{N} é divisivel por 2 e 3")
    N = int(input())