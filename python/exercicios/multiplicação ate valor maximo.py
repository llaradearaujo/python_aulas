import os
os.system("cls || clear")

numero = float(input("digite um numero para ser multiplicado:  "))
multiplicador = float(input("digite um numero multiplicador: "))

resultado = numero
contagem = 0 

while resultado <= 100:
    resultado *= multiplicador
    contagem += 1

print(f"produto final é: {resultado}")
print(f"numero  de multiplicações realizadas: {contagem}")

    