"""
Faça um programa que permaneça em laço até que seja digitado um valor menor ou igual a zero. Cada valor válido
(positivo) digitado deve ser inserido em uma lista na posição imediatamente antes do primeiro elemento que seja
maior que valor que está sendo inserido. Isso resultará em uma lista ordenada de forma crescente. Será
necessário usar o método insert da lista – pesquise sobre ele.
"""

Lista = []
Valor = int(input(" Valor: "))
if Valor > 0:
    Lista.append(Valor)
    Valor = int(input(" Valor: "))
    while Valor > 0:
        i = 0
        Inseriu = False
        while not Inseriu and i < len(Lista):
            if Valor < Lista[i]:
                Lista.insert(i, Valor)
                Inseriu = True
            i += 1
        if not Inseriu:
            Lista.append(Valor)
        Valor = int(input(" Valor: "))
    print('\nSua Lista:')
    for k in Lista:
        print(k, end="  ")
else:
    print('\nSua Lista está vazia!')

print("\n\nFim do programa")