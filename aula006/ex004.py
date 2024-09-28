"""
Reescreva um programa do exercício acima considerando exclusivamente os números positivos
fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem
"número inválido" e o valor deve ser ignorado
"""

N = int(input())
i = 0
V_anterior = 0

while i < N:
    V = float(input())
    if V > 0:
        if V > V_anterior:
            Maior = V
            Menor = V_anterior
        else:
            Maior = V_anterior
            Menor = V
        print(f"Maior: {Maior}")
        print(f"Menor: {Menor}")
        V_anterior = V
    else:
        print("Numero Inválido")
    i += 1
