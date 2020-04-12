#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil, floor
tamanho = float(input("Tamanho da área a ser pintada: "))
litro = tamanho / 6

latas = litro / 18
galoes = litro / 3.6
latas_arredondado = ceil(latas)
galoes_arredondado = ceil(galoes)

latas_baixo = floor(latas)
latas_subtrair = latas_baixo * 18
resto = litro - latas_subtrair
galoes_resto = resto / 3.6
galoes_resto_arredondado = ceil(galoes_resto)
preco_galao_resto = galoes_resto_arredondado * 25
preco_lata_baixo = latas_baixo * 80
preco_total_misturado = preco_lata_baixo + preco_galao_resto

preco_lata = latas_arredondado * 80
preco_galao = galoes_arredondado * 25


print("1: Latas: ", latas_arredondado, " / Preco: ", preco_lata, "\n")
print("2: Galão: ", galoes_arredondado, " / Preco: ", preco_galao, "\n")
print("3: Latas: ", latas_baixo, " / Galões: ", galoes_resto_arredondado, " / Preco: ", preco_total_misturado)
