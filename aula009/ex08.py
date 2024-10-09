"""
Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora
do intervalo [Min, Max] sejam inseridos em uma segunda lista chamada R. Apresentar na tela
a lista de valores aceitos (lista A) e a lista de valores rejeitados (lista R), bem como o
tamanho de cada um
"""

Lista_A = []
Lista_R = []
Tamanho_A = 0
Tamanho_R = 0
Aux = 0
print("\nDigite valores Max e Min:")
LMin = int(input("  Mínimo: "))
LMax = int(input("  Máximo: "))

if LMin > LMax:
    Aux = LMin
    LMin = LMax
    LMax = Aux

N = int(input("Numeros a serem digitados: "))
while N <= 0:
    print("Número deve ser maior que zero!")
    N = int(input("Numeros a serem digitados: "))

print("\nDigite seus valores:")
i = 0
while i < N:
    Valor = int(input(f"    Valor {i+1}: "))
    if Valor >= LMin and Valor <= LMax:
        Lista_A.append(Valor)
        Tamanho_A += 1
    else:
        Lista_R.append(Valor)
        Tamanho_R += 1
    i += 1

print("\nSuas listas:\n")
print(f"Intervalo: {LMin} ; {LMax}")
if Tamanho_A > 0:
    print(f"Lista Aceitos: {Lista_A}")
else:
    print(f"Lista Aceitos: --")
print(f"Tamanho: {Tamanho_A}")
if Tamanho_R > 0:
    print(f"Lista Rejeitados: {Lista_R}")
else:
    print(f"Lista Rejeitados: --")
print(f"Tamanho: {Tamanho_R}")


print("\nFim do programa")