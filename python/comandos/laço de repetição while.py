import os
os.system("cls || clear")

continua = "s"
contador = 0

while continua == "s":
    print("repetindo")

    contador += 1 # = á contador = contador + 1
    continua = input("tecle 's' se deseja continuar: ").strip().lower() #strip= apaga o espaço #lower= deixa qualquer caracter minusculo
   
    #repete enquanto for verdadeiro
    #usado quando não se sabe quantas vezes por acontecer a repetição

if contador == 0:
    print("o bloco não foi repetido")
else:
    print(f"o bloco foi repetido {contador} vezes")
    
