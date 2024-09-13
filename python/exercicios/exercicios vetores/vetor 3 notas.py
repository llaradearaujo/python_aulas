import os
os.system("cls || clear")

notas =  []

for i in range (3):
    nota_inserida = float(input("digite sua nota: "))
    notas.append(nota_inserida)

for i, nota_inserida in enumerate(notas):
    print(f"{i+1}ª nota inserida: {nota_inserida}")