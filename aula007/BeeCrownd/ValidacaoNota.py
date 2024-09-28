"""
Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule
e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota
válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.
"""

Soma = 0
i = 0

while i < 2:
    N = float(input())
    while N < 0 or N > 10:
        print("nota invalida")
        N = float(input())
    Soma += N
    i += 1

Media = Soma / 2

print(f"media = {Media:.2f}")