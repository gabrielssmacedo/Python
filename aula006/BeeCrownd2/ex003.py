S = int(input())

Horas = S // 3600
Resto = S % 3600
Minutos = Resto // 60
Resto = Resto % 60
Segundos = Resto

print(f"{Horas}:{Minutos}:{Segundos}")