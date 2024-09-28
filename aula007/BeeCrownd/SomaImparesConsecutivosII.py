"""
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste
de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y
"""

N = int(input())
Maior = 0
Menor = 0
Lista = []
i = 0
k = 0

while i < N:
    Soma = 0
    S = input().split()
    X = int(S[0])
    Y = int(S[1])
    if X >= Y:
        Maior = X
        Menor = Y
    else:
        Maior = Y
        Menor = X
    while Menor+1 < Maior:
        if (Menor+1) % 2 != 0:
            Soma += Menor+1
        Menor += 1
    Lista.append(Soma)
    i += 1

for k in Lista:
    print(k)
