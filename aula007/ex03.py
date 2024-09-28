# Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-a na tela na
# ordem inversa à ordem de leitura.

Lista = []
i = 0
indice = 0

print("Digite sua Lista com 10 elementos:")
while i < 10:
    E = input(f">> Elemento {i+1}: ")
    Lista.insert(indice,E)
    i += 1

print("\nSua lista invertida é:")
print(Lista)

print("\nFim do Programa")
