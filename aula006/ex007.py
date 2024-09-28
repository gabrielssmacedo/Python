"""
Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor
negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo
usuário, a quantidade de valores, a soma e a média de todos.
"""

i = 0
N = int(input("N: "))
Maior = N
Menor = N
Cont = 0
Soma = 0


while N > 0:
    if N > Maior:
        Maior = N
    if N < Menor:
        Menor = N
    Cont += 1
    Soma = Soma + N
    N = int(input("N: "))

Media = Soma / Cont
print(f"Maior: {Maior}")
print(f"Menor: {Menor}")
print(f"Total Numeros: {Cont}")
print(f"Soma Total: {Soma}")
print(f"Media Total: {Media:.2f}")

with open('Informacoes.txt', 'w') as arquivo:
    arquivo.write("Maior: " + str(Maior) + '\n')
    arquivo.write("Menor: " + str(Menor) + '\n')
    arquivo.write("Total Numeros: " + str(Cont) + '\n')
    arquivo.write("Soma Total: " + str(Soma) + '\n')
    arquivo.write("Media Total: " + str(Media) + '\n')