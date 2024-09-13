import os
os.system("cls || clear")

#entrada
lista_notas = []

for i in range(2):
    nota = float(input("digite uma nota: "))
    lista_notas.append(nota) #coloca valor digitado pelo usuário dentro de um vetor

#saida de dados
for nota in lista_notas:
    print(f"NOTA: {nota}")