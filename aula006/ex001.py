"""
Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10
para esse número fornecido. Siga o formato apresentado abaixo (supondo que foi digitado 4):

"""

N = int(input())
i = 0
tabuada = 10
resultado = 0

while i < tabuada:
    resultado = N * (i+1)
    print(f"{N} x {i+1} = {resultado}")
    with open('tabuada.txt','a') as arquivo:
        arquivo.write(str(N) + ' x ' + str(i+1) + ' = ' + str(resultado) + '\n')
    i += 1