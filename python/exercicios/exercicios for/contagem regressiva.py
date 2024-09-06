import os
os.system("cls || clear")
import time

numero = int(input("digite um numero: "))

print("contagem regressiva do número escolhido: ")

for i in range(numero, 0, -1):
    print (i)
    time.sleep(1)

print("=====fim=====")