N = int(input())

C100 = N // 100
Resto = N % 100
C50 = Resto // 50
Resto = Resto % 50
C20 = Resto // 20
Resto = Resto % 20
C10 = Resto // 10
Resto = Resto % 10
C5 = Resto // 5
Resto = Resto % 5
C2 = Resto // 2
Resto = Resto % 2
C1 = Resto // 1

print(N)
print(f"{C100} nota(s) de R$ 100,00")
print(f"{C50} nota(s) de R$ 50,00")
print(f"{C20} nota(s) de R$ 20,00")
print(f"{C10} nota(s) de R$ 10,00")
print(f"{C5} nota(s) de R$ 5,00")
print(f"{C2} nota(s) de R$ 2,00")
print(f"{C1} nota(s) de R$ 1,00")


