'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
'''

quant_hora = input("Quanto você ganha por hora? R: ")
horas_mes = input("Quantas horas você trabalha no mês? R: ")
salario = float(quant_hora) * int(horas_mes)

ir = float(salario) * 0.11
inss = float(salario) * 0.08
sindicato = float(salario) * 0.05
salario_liquido = float(salario) - float(ir) - float(inss) - float(sindicato)

print("Salário bruto: ", salario, "\nIR: ", ir, "\nINSS: ", inss, "\nSindicato ", sindicato, "\nSalário Liquido: ", salario_liquido)
