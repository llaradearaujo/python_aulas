import os 
os.system("cls || clear")

numeros = []

def tirando_negativos(n):
    numeros_finais = []
    for numeros in n:
        if numeros < 0:
            numeros_finais.append(0)
        else: 
            numeros_finais.append(numeros)
    return numeros_finais

for i in range(5):
    num = int(input("digite um numero: "))
    numeros.append(num)

final = tirando_negativos(numeros)
print(final)