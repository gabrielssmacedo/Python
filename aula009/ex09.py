"""
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente na lista. Neste exercício
é permitido usar os operadores in e/ou not in.
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

while k < N:
    if Lista[k] == NProcura:
        Achou = True
    k += 1

if not Achou:
    print("\nNúmero não encontrado!")
    print("\nFim do Programa")
else:
    print(f"Número {NProcura} encontrado!")
    print("\nFim do Programa")

