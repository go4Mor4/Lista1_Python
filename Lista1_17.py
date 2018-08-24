import math
tamanho = input("Tamanho da área a ser pintada: ")
litro = float(tamanho) / 6

latas = float(litro) / 18
galoes = float(litro) / 3.6
latas_arredondado = math.ceil(latas)
galoes_arredondado = math.ceil(galoes)

latas_baixo = math.floor(latas)
latas_subtrair = float(latas_baixo) * 18
resto = float(litro) - float(latas_subtrair)
galoes_resto = float(resto) / 3.6
galoes_resto_arredondado = math.ceil(galoes_resto)
preco_galao_resto = float(galoes_resto_arredondado) * 25
preco_lata_baixo = float(latas_baixo) * 80
preco_total_misturado = float(preco_lata_baixo) + float(preco_galao_resto)

preco_lata = float(latas_arredondado) * 80
preco_galao = float(galoes_arredondado) * 25


print("1: Latas: ", latas_arredondado, " / Preco: ", preco_lata, "\n")
print("2: Galão: ", galoes_arredondado, " / Preco: ", preco_galao, "\n")
print("3: Latas: ", latas_baixo, " / Galões: ", galoes_resto_arredondado, " / Preco: ", preco_total_misturado)
