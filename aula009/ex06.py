"""
Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os
em uma lista A somente se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora
deste intervalo devem ser ignorados. Ao final,apresentar a lista A e seu tamanho efetivo.
Observe que para este programa funcionar apropriadamente é necessário que LMin seja menor
que LMax. Caso o usuário digite LMax menor que LMin, o programa deve inverter os valores
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

print("\nDigite seus valores:")

Tamanho = 0
i = 0
while i < 10:
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