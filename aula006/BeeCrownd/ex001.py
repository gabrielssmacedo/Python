N = int(input())
i = 0
S_coelhos = 0
S_ratos = 0
S_sapos = 0

while i < N:
    S = input()
    Lista = S.split()
    QTD = int(Lista[0])
    Tipo = Lista[1]
    if Tipo == 'C':
        S_coelhos = S_coelhos + QTD
    elif Tipo == 'R':
        S_ratos = S_ratos + QTD
    elif Tipo == 'S':
        S_sapos = S_sapos + QTD
    i += 1

Cobaias = S_coelhos + S_ratos + S_sapos
P_coelhos = (S_coelhos * 100) / Cobaias
P_ratos = (S_ratos * 100) / Cobaias
P_sapos = (S_sapos * 100) / Cobaias

print(f"Total: {Cobaias} cobaias")
print(f"Total de coelhos: {S_coelhos}")
print(f"Total de ratos: {S_ratos}")
print(f"Total de sapos: {S_sapos}")
print(f"Percentual de coelhos: {P_coelhos:.2f} %")
print(f"Percentual de ratos: {P_ratos:.2f} %")
print(f"Percentual de sapos: {P_sapos:.2f} %")



