import os
os.system("cls || clear")

numeros_checados = []

for i in range(6):
    while True:
        numeros = int(input(f"digite o {i+1}º número: "))

        if (numeros > 0) and (numeros % 2 == 0):
            numeros_checados.append(numeros)
            break


for numeros in reversed(numeros_checados):
    print(numeros)
