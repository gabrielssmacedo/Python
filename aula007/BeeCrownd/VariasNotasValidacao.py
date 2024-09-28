"""
Escreva um programa para ler as notas da primeira e a segunda avaliação de um aluno. Calcule e imprima a média
semestral. O programa só deverá aceitar notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada
nota deve ser validada separadamente.
No final deve ser impressa a mensagem “novo calculo (1-sim 2-nao)”, solicitando ao usuário que informe um código
(1 ou 2) indicando se ele deseja ou não executar o algoritmo novamente, (aceitar apenas os código 1 ou 2). Se for
informado o código 1 deve ser repetida a execução de todo o programa para permitir um novo cálculo, caso contrário
o programa deve ser encerrado.
"""

Repetir = 1

while Repetir == 1:
    Soma = 0
    N1 = float(input())

    while N1 > 10 or N1 < 0:
        print("nota invalida")
        N1 = float(input())

    Soma += N1
    N2 = float(input())

    while N2 > 10 or N2 < 0:
        print("nota invalida")
        N2 = float(input())

    Soma += N2

    Media = Soma / 2
    print(f"media = {Media:.2f}")

    Repetir = int(input("novo calculo (1-sim 2-nao)\n"))

    while Repetir < 1 or Repetir > 2:
        Repetir = int(input("novo calculo (1-sim 2-nao)\n"))
