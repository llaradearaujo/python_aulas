import os
os.system("cls || clear")

contador = 0
soma = 0 

while True:
    nota = float(input("digite sua nota: "))
    contador = contador + 1 
    soma += nota

    inserir_nota = input("deseja inserir mais uma nota? ").upper()
    
    if inserir_nota == "N":
        break

    
media = soma / contador
print(f"a sua média aritmetica é: {media}.") 