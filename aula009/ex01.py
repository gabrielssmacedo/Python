"""
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela um elemento
por linha.
"""
print("Digite 10 valores: ")
Lista = []
N = 10

i = 0
while i < N:
    Valor = float(input(f"Valor {i+1}: "))
    Lista.append(Valor)
    i += 1

print("Valores: ")
k = 0
for k in Lista:
    print(k)