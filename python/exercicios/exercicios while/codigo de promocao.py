import os
os.system("cls || clear")

tentativa = 0
codigo = "promo2024"

while True:
    digite_codigo = input("digite o codigo promocional: ")
    tentativa += 1

    if digite_codigo == codigo:
        print("codigo aceito")
        break
    elif tentativa == 3:
        print("codigo inválido")
        break

