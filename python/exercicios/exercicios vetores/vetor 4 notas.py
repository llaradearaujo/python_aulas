import os
os.system("cls || clear")

notas = []
numero_notas = 4

for i in range(numero_notas):
    notas_inseridas = float(input("digite sua nota: "))
    notas.append(notas_inseridas)

soma = sum(notas)
media = soma/numero_notas

for i, nota in enumerate(notas):
    print(f"{i+1}ª nota: {nota}")

if media >= 7:
    print("aprovado")
if media >= 5 and media < 7:
    print("recuperação")
if media < 5:
    print("reprovado")