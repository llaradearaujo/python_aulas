import os
os.system("cls || clear")

numero = int(input("digite um numero para saber a tabuada dele: "))

print("tabuada do numero escolhido: ")
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")