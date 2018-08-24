import math

tamanho = input("Tamanho da área a ser pintada: ")
litros = int(tamanho) / 3

latas = int(litros) / 18
valor = math.ceil(latas)
preco = int(valor) * 80

print("Latas: ", valor, "\nPreço: ", preco)
