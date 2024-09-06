import os
os.system("cls || clear")

QUANTIA_NOTAS = 3 
soma = 0

for i in range(QUANTIA_NOTAS):
    notas = int(input("digite sua nota: "))
    soma = soma + notas

media = soma/QUANTIA_NOTAS
print(f"sua média: {media}")

if media >= 7:
    print("aprovado")
elif media > 4 and media < 7:
    print("recuperação")
else:
    print("reprovado")
