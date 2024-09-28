"""
Esse programa calcula o total de vendas do Atacado e Varejo. De início recebe as vendas realizadas, bem como os códigos 
dos produtos e a qtd vendida. Se o código é válido a qtd é contabilizada e o Total de vendas é calculado. A qtd de
vendas de cada produto determina o preço unitário para varejo ou atacado, cada produto tem sua Qtd vendas Minima para
Atacado. Os resultados são exibidos ao final do programa.
"""

print("\n------------------------- Vendas: Atacado e Varejo ------------------------\n")
print("Informe a Quantidade de vendas:")

Codigos = [16, 23, 27, 34]
P_Varejo = [14.35, 35.12, 19.35, 63.40]
P_Atacado = [12.93, 29.85, 16.76, 58.25]
QMA = [50, 100, 70, 40]

Total_Varejo = 0
Total_Atacado = 0

NV = int(input("    Número de Vendas: "))
while NV <= 0:
    print("     Número inválido!")
    NV = int(input("    Número de Vendas: "))

print("\nInforme o código do produto e a quantidade de venda:\n")
print("             Cd Qt")
Cont = 0
while Cont < NV:
    S = input(f"    Venda {Cont+1}: ").split()
    Cod = int(S[0])
    QV = int(S[1])
    i = 0
    index = 0
    Validacao = False
    for i in Codigos:
        if Cod == i:
            Validacao = True
            Index = Codigos.index(i)
    if Validacao:
        if QV < QMA[Index]:
            Total_Varejo += P_Varejo[Index] * QV
        else:
            Total_Atacado += P_Atacado[Index] * QV
    else:
        print("     Código Inválido")

    Cont += 1

SomaTotal = Total_Varejo + Total_Atacado

print("\nResultados:\n")
print(f"Total de Vendas do  Grupo de Varejo: R$ {Total_Varejo:.2f}")
print(f"Total de Vendas do  Grupo de Atacado: R$ {Total_Atacado:.2f}")
print(f"Vendas Totais: R$ {SomaTotal:.2f}\n")

print("Fim do Programa")