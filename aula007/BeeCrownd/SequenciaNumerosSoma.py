"""
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for
menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos
inteiros consecutivos entre eles (incluindo o N e M).
"""

i = 0
Printar = ""
Maior = 0
Menor = 0

S = input().split()
M = int(S[0])
N = int(S[1])

while M > 0 and N > 0:
    Soma = 0
    Printar = ""
    if M >= N:
        Maior = M
        Menor = N
    else:
        Maior = N
        Menor = M
    while Menor <= Maior:
        Soma += Menor
        Printar += str(Menor) + " "
        Menor += 1
    Sum = "Sum=" + str(Soma)
    Printar += Sum

    print(Printar)

    S = input().split()
    M = int(S[0])
    N = int(S[1])

