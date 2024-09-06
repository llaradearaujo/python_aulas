import os
os.system("cls || clear")

nota = float(input("digite sua nota: "))

while nota > 10 or nota < 0:
    print("a nota deve ser maior que 0 e menor que 10")
    print(nota)
    nota = float(input("digite sua nota: "))

print(f"a nota é {nota}")

