import os
os.system("cls || clear")

def tabuada(x,y):
    resultado = x*y
    return resultado

numero_multiplicado = int(input("digite o número para saber a tabuada:"))

for i in range(11):
   resultado = tabuada(i,numero_multiplicado)
   print(f"{i} X {numero_multiplicado} = {i*numero_multiplicado}")