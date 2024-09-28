#receber numeros
#verificar quais deles são menores
#ver se a soma é maior que o lado maior
#se sim, classificar qual o tipo de triangulo
from operator import truediv

#Verifica se os lados formam um triangulo e tipo de triangulo

A = float(input("Lado 1: "))
B = float(input("Lado 2: "))
C = float(input("Lado 3: "))

if (A >= B and A >= C) and (B + C) > A:
    Triangulo = True
    l1 = A
    l2 = B
    l3 = C
elif (B >= A and B >= C) and ((A + C) > B):
    Triangulo = True
    l1 = B
    l2 = A
    l3 = C
elif (C >= A and C >= B) and ((A + B) > C):
    Triangulo = True
    l1 = C
    l2 = A
    l3 = B
else:
    Triangulo = False


if Triangulo == True:
    if l1 == l2 and l2 == l3:
        print("Triângulo Equilátero")
    elif l2 == l3:
        print("Triângulo Isósceles")
    elif l2 != l3 and l2 != l1:
        print("Triângulo Escaleno")
    elif (l1 == l2 or l1 == l3) and (l1 > l2 or l1 > l3):
        print("Triângulo Isósceles")
else:
    print("Os lados fornecidos não compõem um triângulo!")