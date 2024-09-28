"""
Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y
uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.
"""

S = input().split()
X = int(S[0])
Y = int(S[1])

while X != Y:

    if X > Y:
        print("Decrescente")
    elif Y > X:
        print("Crescente")
    S = input().split()
    X = int(S[0])
    Y = int(S[1])