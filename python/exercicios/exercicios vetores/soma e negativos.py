import os
os.system("cls || clear")

numeros_reais = []
negativos = []
positivos = []





for i in range(10):
    numeros = float(input("digite um número real: "))
    numeros_reais.append(numeros)

    if numeros < 0:
        negativos.append(numeros)
    else:
        positivos.append(numeros) # append = insere numeros na lista/vetor

quantia_negativos = len(negativos) # len = retorna a quantia de elementos no vetor
soma_positivos = sum(positivos)    # sun = retorna a soma de elementos do vetor


print(f"você digitou {quantia_negativos} numeros negativos")
print(f"a soma dos números positivos é: {soma_positivos}")