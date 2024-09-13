import os
os.system("cls || clear")

numeros = []

for i in range(5):
    numero_digitado = float(input(f"digite o {i+1}º numero: "))
    numeros.append(numero_digitado)
    
maior_numero = max(numeros)
menor_numero = min(numeros)

for contador, numero in enumerate(numeros):
    print(f"{contador + 1}ª numero: {numero}")

print(f"maior numero: {maior_numero}")
print(f"menor numero: {menor_numero}")