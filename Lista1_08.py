#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

quant_hora = input("Quanto você ganha por hora? R: ")
horas_mes = input("Quantas horas você trabalha no mês? R: ")

salario = float(quant_hora) * int(horas_mes)
print("O seu salário no final do mês será de R$", salario)
