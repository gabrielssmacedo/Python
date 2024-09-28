A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

Delta = B**2 - 4 * A * C

if Delta > 0:
    X1 = (-B + Delta**0.5) / (2 * A)
    X2 = (-B - Delta**0.5) / (2 * A)
    print("X1 = %.2f" % X1)
    print("X2 = %.2f" % X2)
elif Delta < 0:
    print("Não há raízes reais")
else:
    X1 = -B / (2 * A)
    print(f"X = %.2f" % X1)


