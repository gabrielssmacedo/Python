"""
Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros
termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número
ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente,
0 e 1.
"""

N = int(input("Termos: "))

i = 0
Termo_Atual = 1
Termo_Anterior = -1
Prox_Termo = 1


while i < N:
    Prox_Termo = Termo_Anterior + Termo_Atual
    Termo_Anterior = Termo_Atual
    Termo_Atual = Prox_Termo
    print(Prox_Termo)
    with open('Fibonacci.txt', 'a') as arquivo:
        arquivo.write(str(Prox_Termo) + '\n')
    i += 1