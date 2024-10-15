"""
Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominados
A e B com os tamanhos nA e nB, respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam
aceitos valores repetidos. Em seguida, o programa deve juntar as duas listas em um única lista R (resultante)
tomando o cuidado de que a lista R não deve ter valores duplicados. Veja o exemplo:
"""

nA = int(input('Tamanho Lista A: '))
nB = int(input('Tamanho Lista B: '))
LA = []
LB = []

Iniciando = True
print('Lista A:')
i = 0
while i < nA:
    Valor = int(input(f'    Valor {i + 1}: '))
    if not Iniciando:
        Repetido = False
        k = 0
        while Repetido == False and k < len(LA): #Verifica se o Valor ja esta na Lista
            if LA[k] == Valor:
                Repetido = True
            k += 1
        if Repetido:
            print(f'\nERRO: elemento {Valor} já está na lista!')
        else:
            LA.append(Valor)
            i += 1
    else:
        LA.append(Valor)
        Iniciando = False
        i += 1

print('\nLista A:', end=" ")
for p in LA:
    print(p, end="  ")

Iniciando = True
print('\n\nLista B:')
i = 0
while i < nB:
    Valor = int(input(f'    Valor {i + 1}: '))
    if not Iniciando:
        Repetido = False
        k = 0
        while Repetido == False and k < len(LB): #Verifica se o Valor ja esta na Lista
            if LB[k] == Valor:
                Repetido = True
            k += 1
        if Repetido:
            print(f'\nERRO: elemento {Valor} já está na lista!')
        else:
            LB.append(Valor)
            i += 1
    else:
        LB.append(Valor)
        Iniciando = False
        i += 1

print('\nLista B:', end=" ")
for p in LB:
    print(p, end="  ")

Resultante = LA[:]

k = 0
while k < nB:
    j = 0
    Existente = False
    while j < nA:
        if LB[k] == LA[j]:
            Existente = True
        j += 1
    if not Existente:
        Resultante.append(LB[k])
    k += 1

print(f'\n\nLista Resultante:')
for j in Resultante:
    print(j, end="  ")

print('\n\nFim do Programa')