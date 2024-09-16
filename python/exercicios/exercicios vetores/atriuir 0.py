import os
os.system("cls || clear")

numeros = []
numero_final = []

for i in range(5):
    numero_digitado = int(input("digite um numero:"))
    numeros.append(numero_digitado)

for numero in numeros:
        if numero < 0:
            numero_final.append(0)
        else:
            numero_final.append(numero)

print(numero_final)
