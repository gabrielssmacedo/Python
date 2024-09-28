N = input().split()
A = int(N[0])
B = int(N[1])
C = int(N[2])

Maior = 0

if A > B:
    MaiorAB = A
else:
    MaiorAB = B

if MaiorAB > C:
    Maior = MaiorAB
else:
    Maior = C

print(f"{Maior} eh o maior")