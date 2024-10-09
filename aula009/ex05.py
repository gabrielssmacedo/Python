"""
Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve
garantir isso em um laço) e em seguida leia N números reais em uma lista A. O programa deve
separar os valores lidos em A em outras duas listas NEG e POS, a primeira contendo somente
os valores negativos e a segunda contendo os valores positivos e zero. Apresentar na tela as
listas NEG e POS e a quantidade de valores contidos em cada uma.
"""

ListaA = []
NEG = []
POS = []
N_positivos = 0
N_negativos = 0

N = int(input("Digite um número: "))
while N <=0 or N >= 50:
    print("O número deve estar entre 0 e 50!\n")
    N = int(input("Digite um número: "))

i = 0
while i < N:
    Valor = float(input(f"  Valor {i+1}: "))
    ListaA.append(Valor)
    i += 1

k = 0
for k in ListaA:
    if k >= 0:
        POS.append(k)
        N_positivos += 1
    else:
        NEG.append(k)
        N_negativos += 1

print("\nSeus números são: \n")
print(f"Negativos: {NEG}\n> Quantidade: {N_negativos}")
print(f"Positivos: {POS}\n> Quantidade: {N_positivos}")
print("\nFim do Programa")