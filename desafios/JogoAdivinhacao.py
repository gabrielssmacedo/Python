"""
Jogo de Adivinhação entre usuário e o computador. O computador sorteia um numero aleatório e o usuário deve tentar
acerta-lo. No final, os resultados são impressos para o usuário.
"""
from random import randint

print("\n------------------------- JOGO DA ADIVINHAÇÃO --------------------------------\n")
print("Um número será sorteado e o seu papel é tentar advinhá-lo com menor \nnúmero de tentativas possível.")
print("Boa Sorte!\n")

Min = int(input(">> Digite Valor mínimo: "))
Max = int(input(">> Digite Valor Máximo: "))

while Min + 100 > Max:
    print("\n OPSS! O número máximo deve ser maior que o mínimo + 100 ! \n")
    Min = int(input(">> Digite Valor mínimo: "))
    Max = int(input(">> Digite Valor Máximo: "))

NumAleatorio = randint(Min, Max)

print("\nAgora é pra valer:")

Cont = 0
Lista = []

while Cont == 0 or Tentativa != NumAleatorio:
    Cont += 1
    Tentativa = int(input(f"    >> Palpite {Cont}: "))
    while Tentativa < Min or Tentativa > Max:
        print("Palpite fora do intervalo !")
        Tentativa = int(input(f"    >> Palpite {Cont}: "))

    Lista.append(Tentativa)

    if Tentativa > NumAleatorio:
        print("Errado: Seu palpite deve ser MENOR")
    elif Tentativa < NumAleatorio:
        print("Errado: Seu palpite deve ser MAIOR")

if Cont == 1:
    print("\nGÊNIOOOOOOOOO !!! Acertou de primeira, sabe muito !!\n")
else:
    print("\nACERTOUUUU !!! \n")

i = 0
Palpites = ""

for i in Lista:
    Palpites += str(i) + " "

print("RESULTADO:\n")
print(f"foram {Cont} palpites até você acertar")
print(f"seus palpites foram esses: {Palpites}")
print("\nFim do Programa")
