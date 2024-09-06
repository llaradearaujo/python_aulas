import os
os.system("cls || clear")

while  True:
    
    nota = float(input("digite sua nota: "))

    if nota < 0 or nota > 10:
        print("a nota deve ser maior que 0 e menor que 10")
        print(f"nota: {nota}")
    else:
        break
