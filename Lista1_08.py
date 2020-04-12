# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
quant_hora = float(input("Quanto você ganha por hora? R: "))
horas_mes = int(input("Quantas horas você trabalha no mês? R: "))

salario = quant_hora * horas_mes
print("O seu salário no final do mês será de R$", salario)
