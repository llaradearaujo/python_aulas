import os
os.system("cls || clear")

numeros = []
numeros_pares = 0
numeros_impares = 0 

def verificar_pares_impares(numeros):
    numeros_pares = 0
    numeros_impares = 0 
    
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
   
    return numeros_pares, numeros_impares


for i in range(6):
    numeros_digitados = float(input("digite um numero: "))
    numeros.append(numeros_digitados)


numeros_pares, numeros_impares = verificar_pares_impares(numeros)


for i, numero in enumerate(numeros):
    print(f"{i+1}º numero: {numero}")

print(f"numeros pares informados {numeros_pares}")
print(f"numeros impáres informados: {numeros_impares}")

