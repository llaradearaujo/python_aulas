import os
os.system("cls || clear ")

contagem_numero = 0
soma = 0 

while True:
    inserir_numero = int(input("digite um número inteiro: "))

    if inserir_numero % 2 != 0:
        soma = soma + inserir_numero
        contagem_numero += 1 
        
        if soma > 200:
            break

print(f"o total de numeros ímpares inseridos foi {contagem_numero}")
print(f"a soma dos números impares inseridos é {soma}")