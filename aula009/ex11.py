"""
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000. Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e, caso X
esteja na lista, deve eliminá-lo. Caso haja várias ocorrências de X, todas devem ser eliminadas. Pesquise como
usar a função del (você vai precisar dela e neste exercício será permitido usá-la).
"""
from random import randint

N  = int(input("Tamanho da Lista: "))
Lista = []

for i in range(N):
    Valor = randint(0, 5)
    Lista.append(Valor)

print('\nSua Lista:')
for i in Lista:
    print(i, end="  ")

X = int(input('\n\nRemover elemento: '))

Removido = False
k = 0
while k < len(Lista):
    if Lista[k] == X:
        del Lista[k]
        Removido = True
        k = -1
    k += 1

if Removido:
    print(f'\nElemento {X} removido com sucesso nas posições:')
    print('Sua Lista:')
    for i in Lista:
        print(i, end="  ")
else:
    print(f'Elemento {X} não está na lista!')

print('\n\nFim do programa')
