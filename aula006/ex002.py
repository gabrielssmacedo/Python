"""
Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.

"""

Max = int(input("Max: "))
Min = int(input("Min: "))

while Min > Max:
    print("O valor Máximo deve ser maior que o Minimo!")
    Max = int(input())
    Min = int(input())

while Min < Max:
    if (Min+1) % 5 == 0:
        print(Min+1)
    Min += 1