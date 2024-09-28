#Escreva um programa que permaneça em laço até que seja digitado o valor zero ou negativo. Cada valor
#positivo lido deve ser inserido no final de uma lista, usando o metodo append. Ao final exiba a lista
#completa na tela.

Lista = []
N = int(input("Digite um número: "))

if N > 0:
    while N > 0:
        Lista.append(N)
        N = int(input("Digite um número: "))
    print("\nSua lista é:")
    print(Lista)
else:
    print("\nSua lista está vazia!")

print("\nFim do programa")

