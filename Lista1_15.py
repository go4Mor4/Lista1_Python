quant_hora = input("Quanto você ganha por hora? R: ")
horas_mes = input("Quantas horas você trabalha no mês? R: ")
salario = float(quant_hora) * int(horas_mes)

ir = float(salario) * 0.11
inss = float(salario) * 0.08
sindicato = float(salario) * 0.05
salario_liquido = float(salario) - float(ir) - float(inss) - float(sindicato)

print("Salário bruto: ", salario, "\nIR: ", ir, "\nINSS: ", inss, "\nSindicato ", sindicato, "\nSalário Liquido: ", salario_liquido)
