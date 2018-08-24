'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''

fahrenheit = input("Quantidade de graus Fahrenheit: ")
celsius = (float(fahrenheit) - 32) / 1.8

print(fahrenheit, " graus Fahrenheit são iguais a ", celsius, " graus celsius")
