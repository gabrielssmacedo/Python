"""
. Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o
programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim.
"""

Prim = int(input("Prim: "))

N = int(input("Termos: "))

i = 0
Termo_Atual = 1
Termo_Anterior = -1
Prox_Termo = 1

while i < N:
    Prox_Termo = Termo_Anterior + Termo_Atual
    Termo_Anterior = Termo_Atual
    Termo_Atual = Prox_Termo
    if Prox_Termo > Prim:
        print(Prox_Termo)
        with open('Fibonacci2.txt', 'a') as arquivo:
            arquivo.write(str(Prox_Termo) + '\n')
        i += 1