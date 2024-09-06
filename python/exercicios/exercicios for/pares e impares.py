import os
os.system("cls || clear")

pares = 0
impares = 0

for i in range(5):
    numero = int(input("digite um número:"))
    if numero % 2 == 0: #porcentagem serve para pegar o resto( se numero dividido por dois tem resto 0 escreva par)
        pares = pares + 1
    else:
       impares = impares + 1

print (f"quantia de numeros pares: {pares}")
print(f"quantia de numeros impáres: {impares}")
    #!= significa diferente