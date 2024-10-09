"""
Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado,
onde N é um número fornecido pelo usuário. Esse N deve ser usado no programa ao invés do
tamanho fixo de 10 sugerido no programa anterior.
"""
Lista = []
Aux = 0
print("\nDigite valores Max e Min:")
LMin = int(input("  Mínimo: "))
LMax = int(input("  Máximo: "))

if LMin > LMax:
    Aux = LMin
    LMin = LMax
    LMax = Aux

Tamanho = 0
N = int(input("Numeros a serem digitados: "))
while N <= 0:
    print("Número deve ser maior que zero!")
    N = int(input("Numeros a serem digitados: "))

print("\nDigite seus valores:")
i = 0
while i < N:
    Valor = int(input(f"    Valor {i+1}: "))
    if Valor >= LMin and Valor <= LMax:
        Lista.append(Valor)
        Tamanho += 1
    i += 1

if Tamanho > 0:
    print("\nSua lista:\n")
    print(f"Intervalo: {LMin} ; {LMax}")
    print(f"Valores: {Lista}")
    print(f"Tamanho: {Tamanho}")
else:
    print("\nSua lista:\n")
    print(f"Intervalo: {LMin} ; {LMax}")
    print("Sua Lista está vazia!")

print("\nFim do programa")