"""
Faça um programa que permaneça em laço até que seja digitado um valor menor ou igual a zero. Cada valor válido
(positivo) digitado deve ser inserido em uma lista na posição imediatamente antes do primeiro elemento que seja
maior que valor que está sendo inserido. Isso resultará em uma lista ordenada de forma crescente. Será
necessário usar o método insert da lista – pesquise sobre ele.
"""

Lista = []

Valor = int(input("Valor: "))
Iniciando = True

if Valor > 0:
    if Iniciando:
        Lista.append(Valor)
        Iniciando = False
    while Iniciando == False and Valor > 0:
        k = 0
        while True:
            if Lista[k] > Valor:
                Lista.insert(k, Valor)
                break
            k += 1
        Valor = int(input("Valor: "))

if Iniciando:
    print("Sua lista está vazia!")

print("\nFim do programa")