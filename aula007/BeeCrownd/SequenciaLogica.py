"""
Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução
do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos
devem ser apresentados.
"""
N = int(input())
while N < 2 or N > 999:
    N = int(input())

i = 0
V1 = 0
V2 = 1
V3 = 0

while i < N:
    V1 += 1
    V2 = V1**2
    V3 = V1 * V2
    print(V1, V2, V3, sep=' ')
    V2 += 1
    V3 = (V1 * V2) - (V1 - 1)
    print(V1, V2, V3, sep=' ')
    i += 1