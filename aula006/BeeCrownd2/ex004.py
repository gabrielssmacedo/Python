S = input().split()
A = int(S[0])
B = int(S[1])
C = int(S[2])
D = int(S[3])

C1 = B > C
C2 = D > A
C3 = (C+D) > (A+B)
C4 = C > 0 and D > 0
C5 = (A % 2) == 0

if C1 and C2 and C3 and C4 and C5:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")