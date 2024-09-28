"""
Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N,
onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse
requisito).
"""

i = 0
N = int(input("N: "))
Soma = 0

while N < 100:
    print("Digite um número maior/igual a 100!")
    N = int(input("N: "))

while i <= N:
    if i % 2 == 0:
       Soma = Soma + i
    i += 1

print(f"Soma pares = {Soma}")
with open('Soma.txt', 'w') as arquivo:
    arquivo.write("Soma pares = " + str(Soma) + '\n')