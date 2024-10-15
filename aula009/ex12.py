"""
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros digitados pelo
usuário. Exiba na tela a lista preenchida. Em seguida, o programa deve procurar e eliminar os elementos que
eventualmente estiverem repetidos deixando apenas a primeira ocorrência de cada valor. Apresentar a lista
resultante na tela.
"""
from random import randint

N = int(input('Tamanho da Lista: '))
Lista = []
Min = 0
Max = 10

for i in range(N):
    Valor = randint(Min, Max)
    Lista.append(Valor)

print('Lista gerada:')
for i in Lista:
    print(i, end="  ")

Len_Antes = len(Lista)

i = 0
while i < len(Lista):
    j = i + 1
    while j < len(Lista):
        if Lista[i] == Lista[j]:
            del Lista[j]
            j -= 1
        j += 1
    i += 1

Len_Depois = len(Lista)

if Len_Antes == Len_Depois:
    print('\n\nNão há elementos repetidos na Lista!')
else:
    print('\n\nElementos repetidos removidos com sucesso!')
    print('\nLista Final:')
    for i in Lista:
        print(i, end="  ")


print('\n\nFim do programa')
