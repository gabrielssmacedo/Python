"""
Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes
tamanhos nA e nB, respectivamente. Em seguida o programa deve juntar as duas listas em uma única lista com o
tamanho nA+nB. Exibir na tela a lista resultante. Veja o exemplo:
"""

nA = int(input("Tamanho Lista A: "))
nB = int(input("Tamanho Lista B: "))
LA = []
LB = []

i = 0
print("\nLista 1:")
while i < nA:
        Valor = int(input(f"    Valor {i+1}: "))
        LA.append(Valor)
        i += 1

print("\nLista 2:")
i = 0
while i < nB:
    Valor = int(input(f"    Valor {i+1}: "))
    LB.append(Valor)
    i += 1

Lista = LA + LB

print(f"\nSua lista:\n{Lista}")
print("\nFim do Programa")