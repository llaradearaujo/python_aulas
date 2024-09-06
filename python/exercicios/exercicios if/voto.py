import os
os.system("cls || clear")

#solicitar dados 
idade = int(input("qual a sua idade?"))

#verificar
if idade < 18 or idade > 65:
    print("seu voto não é obrigatório!")
else:
    print("seu voto é obrigatório!")
