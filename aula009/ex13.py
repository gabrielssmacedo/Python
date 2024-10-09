"""
Escreva um programa que leia um número inteiro N. Em seguida calcule e armazene em uma lista os N primeiros
números primos. Exibir a lista no final. Ex. se N fornecido pelo usuário for 10, então a lista será carregada com:
V: 2 3 5 7 11 13 17 19 23 29
"""

N = int(input("Primeiros Números Primos: "))
Primos = []

Numero = 2
i = 0
while i < N:
    Divisao = 0
    k = 2
    while k < Numero:
        if Numero % k == 0:
            Divisao += 1
        k += 1
    if Divisao == 0:
        Primos.append(Numero)
        i += 1
    Numero += 1

print(f"{N} primeiro(s) primo(s):")
print(f"{Primos}")
print("\nFim do Programa")
