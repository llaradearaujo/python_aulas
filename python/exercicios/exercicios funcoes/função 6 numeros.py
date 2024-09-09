import os
os.system("cls || clear")


def pares_impares():
    contador_par = 0
    contador_impar = 0

    for i in range(6):
        numero = int(input("digite um numero: "))
        if numero % 2 == 0:
            contador_par += 1
        else: 
            contador_impar += 1  

    print(f"voce inseriu {contador_par} números pares")
    print(f"voce inseriu {contador_impar} números ímpares")

#chamando a função
pares_impares()