import os 
os.system("cls||clear")

def impar_par (x):
    if x % 2 != 0:
        return print("este número é impar")
    else:
        return print("este número é par")

numero = int(input("digite um número: "))

resultado = impar_par(numero)


