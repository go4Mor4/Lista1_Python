import math

tamanho = input("Digite o tamanho do arquivo: ")
velocidade = input("Digite a velocidade da internet: ")

tempo = float(tamanho) / float(velocidade)
minutos = math.ceil(float(tempo) / 60)

print("O arquivo levará ", minutos, "minutos para ficar pronto")
