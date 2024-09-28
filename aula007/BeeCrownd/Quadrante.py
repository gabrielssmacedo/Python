"""
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos
no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo
será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).
"""

S = input().split()
X = int(S[0])
Y = int(S[1])

while X != 0 and Y != 0:
    if X > 0 and Y > 0:
        print("primeiro")
    elif X < 0 and Y > 0:
        print("segundo")
    elif X < 0 and Y < 0:
        print("terceiro")
    elif X > 0 and Y < 0:
        print("quarto")
    S = input().split()
    X = int(S[0])
    Y = int(S[1])