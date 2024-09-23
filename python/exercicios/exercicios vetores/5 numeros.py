import os
os.system("cls || clear")

#declarando variáveis
lista_numeros = []
positivos = 0
negativos = 0 
pares = 0
impares = 0

#processando dados
while True: 
    numero = (int(input("digite um numero ou digite 0 para ver resultados: ")))
    os.system("cls || clear")
    
    if numero != 0:
        lista_numeros.append(numero)

    if numero > 0:
        positivos += 1
    elif numero == 0:
        break
    else:
        negativos += 1

    if numero % 2 == 0 and numero > 0:
        pares += 1 
    elif numero % 2 != 0:
        impares += 1

#verificando quantidade de numeros inseridas
total_numeros = len(lista_numeros)

#mostrando dados
print("exibindo resultados")
print(f"quantidade de pares positivos: {pares}")
print(f"quantidade de impares: {impares}")
print(f"quantidade de positivos: {positivos}")
print(f"quantidade de negativos: {negativos}")
print(f"quantidade total de numeros inseridos: {total_numeros}")







