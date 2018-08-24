'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
'''

inteiro1 = input("Digite um número inteiro: ")
inteiro2 = input("Digite outro número inteiro: ")
real = input("Digite um número real")

a = (int(inteiro1) * 2) + (int(inteiro2) / 2)
b = (int(inteiro1) * 3) + float(real)
c = float(real) ** 3

print("a : ", a, "\nb : ", b, "\nc : ", c)
