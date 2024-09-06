import os
os.system("cls||clear")

contador = 0 

while True:
    numero = int(input("digite um numero negativo para ser contabilizado: "))
    if numero < 0:
        contador += 1
    else:
        break

print(f"foram contabilizados {contador} numeros negativos")