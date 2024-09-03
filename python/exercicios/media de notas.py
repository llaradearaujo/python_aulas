import os
os.system("cls || clear")

numero_notas = 0
soma = 0
notas = 0

while True:
    valor_notas = float(input("digite sua nota: "))
    if valor_notas >= 0:
        numero_notas += 1
        soma = soma + valor_notas
    else:
        break
    

media = soma/numero_notas
print(f"sua média é: {media}")