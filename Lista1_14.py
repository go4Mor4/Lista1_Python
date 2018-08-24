peso = input("Digite o peso dos peixes: ")
execesso = int(peso) - 50
multa = int(execesso) * 4

if execesso < 1:
    print("João não terá que pagar multa")
else:
    print("A multa que joão terá que pagar será de: ", multa)
