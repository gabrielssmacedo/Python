#Ta errado

CDGP1, QTD1, V1 = input().split()
CDGP2, QTD2, V2 = input().split()

QTD1 = int(QTD1)
V1 = float(V1)
QTD2 = int(QTD2)
V2 = float(V2)

Total = QTD1 * V1 + QTD2 * V2

print("VALOR A PAGAR: R$ %.2f"% Total)