import os
os.system("cls || clear")

#funções
def pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def impares(numeros):
    impares = []
    for numero in numeros:
        if numero % 2 != 0:
            impares.append(numero)
    return impares

def positivos(numeros):
    positivos = [] 
    for numero in numeros:
        if numero >= 0:
            positivos.append(numero)
    return positivos

def negativos(numeros):
    negativos = []
    for numero in numeros:
        if numero < 0:
            negativos.append(numero)
    return negativos
        

#declarando listas
todos_numeros = []
numeros_invertidos = [] 


print("\n======= Solicitando Dados ======= ")
for i in range(5):
    numeros = int(input(f"Digite o {i+1}º numero: "))
    todos_numeros.append(numeros)


#dando valores as funções
numeros_negativos = negativos(todos_numeros)
numeros_positivos = positivos(todos_numeros)
numeros_pares = pares(todos_numeros)
numeros_impares = impares(todos_numeros)

#calculando maior e menor numero
maior_numero = max(todos_numeros)
menor_numero = min(todos_numeros)

#somando numeros
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)
soma_total = sum(todos_numeros)

#calculando quantias
quantia_pares = len(numeros_pares)
quantia_impares = len(numeros_impares)
quantia_positivos = len(numeros_positivos)
quantia_negativos = len(numeros_negativos)
quantia_total = len(todos_numeros)

#fazendo médias
media_pares = soma_pares / quantia_pares
media_impares = soma_impares / quantia_impares
media_total = soma_total / quantia_total


#mostrando numeros invertidos
for numero in reversed(todos_numeros):
    numeros_invertidos.append(numero)


#imprimindo as estatísticas
print("\n====== Exibindo Resultados =======")
print(f"Quantidade de números inseridos: {quantia_total}")
print(f"Quantidade de pares: {quantia_pares}")
print(f"Quantidade de ímpares: {quantia_impares}")
print(f"Quantidade de positivos: {quantia_positivos}")
print(f"Quantidade de negativos: {quantia_negativos}")
print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média dos números ímpares: {media_impares:.2f}")
print(f"Média de todos os números: {media_total:.2f}")
print(f"Ordem invertida dos numeros: {numeros_invertidos}")