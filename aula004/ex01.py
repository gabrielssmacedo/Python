A = int(input("A:"))
B = int(input("B:"))

if B == 0:
    print("Não é possível realizar a divisão por 0!")
else:
    R = A / B
    print("Resultado: %.20f" % R)
    print(type(B))