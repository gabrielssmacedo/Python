"""
Desenvolva um programa que leia do teclado um número inteiro e mostre na tela se esse número é
primo ou não. Lembrando: um número primo é divisível somente por 1 e por ele mesmo.
"""

N = int(input("N: "))

i = 1
Divisores = 0

while i <= N:
    if N % i == 0:
        Divisores += 1
    i += 1

if Divisores < 3:
    print(f"{N} é primo")
    with open('primo.txt', 'w') as arquivo:
        arquivo.write(str(N) + " e primo" + '\n')
else:
    print(f"{N} não é primo")
    with open('primo.txt', 'w') as arquivo:
        arquivo.write(str(N) + " nao e primo" + '\n')