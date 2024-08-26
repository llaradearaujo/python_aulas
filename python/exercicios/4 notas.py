import os
os.system("cls || clear")

soma = 0
for i in range(4):
    nota = float(input("digite sua nota:"))
    soma = soma + nota

media = soma/4

print(f"sua média é {media}")