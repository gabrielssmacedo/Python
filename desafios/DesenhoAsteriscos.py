"""
Esse programa recebe um número X do usuário e exibe um quadrado com X asteriscos de lado. O quadrado
não possui pontas, é oco por dentro e possui uma parede de 2 asteriscos (parececido com um '0' pixelado)
"""

print("\n--------------------- Desenho com Asteriscos ---------------------------\n")
print("Você pode escolher o tamanho do desenho ! \n")

i = 0
Min = 6
Max = 32

N = int(input(">> Digite um número: "))
print("\n")
while N % 2 == 1 or N < Min or N > Max:
    print(f"O numero {N} é inválido!\n")
    N = int(input(">> Digite um número: "))
    print("\n")

while i < N:
    if i == 0 or i == N-1:
        j = 0
        print(" ",end="")
        while j < N-2:
            print("*",sep="", end="")
            j += 1
        print(" ")
    elif i == 1 or i == N-2:
        j = 0
        while j < N:
            print("*", sep="", end="")
            j += 1
        print("")
    else:
        j = 0
        while j < N:
            if j < 2 or j > N-3:
                print("*", sep="", end="")
            else:
                print(" ",sep="", end="")
            j += 1
        print("")
    i += 1

print("\nFim do Programa")