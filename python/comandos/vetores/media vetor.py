import os
os.system("cls || clear")

soma = 0
notas =  []

for i in range (3):
    nota_inserida = float(input("digite sua nota: "))
    notas.append(nota_inserida)

soma = sum(notas)#soma todas os componentes do vetor
media = soma/3

for contador, nota in enumerate(notas):#enumera os itens do vetor
    print(f"{contador + 1 }ª nota: {nota}")

print(f"sua média é {media:.1f}")