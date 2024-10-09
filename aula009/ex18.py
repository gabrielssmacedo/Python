"""
O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente,
deve ser maior que Min. Em seguida preencher a lista com todos os valores situados entre Min e Max que sejam
divisíveis por 7. Exibir a lista resultante na tela.
"""
Lista = []
Min = int(input("Min: "))
Max = int(input("Max: "))

while Min > Max:
    print("Valor mínimo deve ser maior que o máximo")
    Min = int(input("Min: "))
    Max = int(input("Max: "))

Min = Min + 1
while Min < Max:
    if Min % 7 == 0:
        Lista.append(Min)
    Min += 1

print(f"Sua Lista:\n{Lista}")
print(f"\nFim do Programa")
