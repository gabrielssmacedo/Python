"""
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela na ordem
inversa à ordem de leitura, sendo um elemento por linha da tela.
"""
"""
#1ºforma
N = 10
L1 = []
print("Digite 10 números:")

i = 0
while i < N:
    Valor = int(input(f"    Valor {i+1}: "))
    L1.append(Valor)
    i += 1

L2 = L1[:]

p = 0
q = N-1
while p < N:
    L1[p] = L2[q]
    p += 1
    q -= 1

j = 0
for j in L1:
    print(j)

"""
#2º Forma

N = 10
Lista = []
print("Digite 10 números:")

i = 0
while i < N:
    Valor = int(input(f"    Valor {i+1}: "))
    Lista.append(Valor)
    i += 1

k = N-1

while k >= 0:
    print(Lista[k])
    k -= 1



