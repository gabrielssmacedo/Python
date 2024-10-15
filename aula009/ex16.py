"""
Escreva um programa que leia uma lista com N números inteiros, onde N é um número inteiro previamente
digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que
quando esta situação ocorrer uma mensagem deve ser dada ao usuário. Por fim exibir na tela a lista resultante.
"""

N = int(input("Numeros lidos: "))
Lista = []

Iniciando = True
i = 0
while i < N:
    Valor = int(input(f'    Valor {i+1}: '))
    if not Iniciando:
        Repetido = False
        k = 0
        while Repetido == False and k < len(Lista): #Verifica se o Valor ja esta na Lista
            if Lista[k] == Valor:
                Repetido = True
            k += 1
        if Repetido:
            print(f'\nERRO: elemento {Valor} já está na lista!')
        else:
            Lista.append(Valor)
            i += 1
    else:
        Lista.append(Valor)
        Iniciando = False
        i += 1


print(f"\nSua Lista:")
for k in Lista:
    print(k, end="  ")

print("\n\nFim do Programa")