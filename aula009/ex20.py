"""
Faça um programa que leia um número inteiro N obrigatoriamente maior que 10. Preencha uma lista de tamanho
N com números inteiros aleatórios. Exiba na tela a lista gerada e em seguida coloque-a em ordem crescente
usando o metodo da bolha. Não é permitido usar o metodo sort da lista
"""
from random import randint

Min = 0
Max = 1000
Lista = []

N = int(input('Tamanho da Lista: '))
while N <= 4:
    print('O tamanho deve ser MAIOR que 10!')
    N = int(input('Tamanho da Lista: '))

for i in range (N):
    Valor = randint(Min, Max)
    Lista.append(Valor)

print('\nLista Desordenada:')
for i in Lista:
    print(i, end=" ")

#ordenando lista com metodo bolha (bubblesort)

for j in range(1, N):
    for i in range(N-j):
        Aux = 0
        if Lista[i] > Lista[i+1]:
            Aux = Lista[i]
            Lista[i] = Lista[i+1]
            Lista[i+1] = Aux

print(f'\n\nLista: {Lista}')

print('Fim do Programa')