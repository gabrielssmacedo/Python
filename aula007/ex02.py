#Refaça o programa anterior, porém ao final exiba na tela cada elemento da lista em uma linha da tela
#(este programa deve exibir um elemento por vez dentro de um laço e usando um índice para acessar
#cada elemento individualmente).

Lista = []
i = 0
N = int(input("Digite um número: "))

if N > 0:
    while N > 0:
        Lista.append(N)
        N = int(input("Digite um número: "))
    print("\nSua lista é:")
    for i in Lista:
        print(f"  {i}")
else:
    print("\nSua lista está vazia!")

print("\nFim do programa")