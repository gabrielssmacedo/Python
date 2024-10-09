"""
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente, bem como informar a
posição de X na lista. Se houver mais de uma ocorrência de X na lista informe todas as posições. Neste exercício
não é permitido usar os operadores in e not in. Também não é permitido usar qualquer função pronta de Python
"""
from random import randint

Lista = []

N = int(input("Digite um número: "))

i = 0

while i < N:
    Valor = randint(0, 1000)
    Lista.append(Valor)
    i += 1

print(f"\nSua lista:\n{Lista}")

NProcura = int(input("\nProcure um valor: "))

k = 0
Achou = False
index = 0
Posicoes = []

while k < N:
    if Lista[k] == NProcura:
        Achou = True
        index = k
        Posicoes.append(index)
    k += 1

if Achou:
    print(f"    Número {NProcura} encontrado em:")
    print(f"    Posições: {Posicoes}")
    print("\nFim do Programa")
else:
    print("Número não encontrado em nenhuma posição!")