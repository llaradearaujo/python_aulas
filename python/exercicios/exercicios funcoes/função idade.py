import os
os.system("cls || clear")

def idade(nascimento):
    idade = 2024 - nascimento
    return idade

#solicitando dados
nascimento = int(input("digite seu ano de nascimento: "))

#processando dados 
idade = idade(nascimento)

#mostrando dados
print(f"você tem {idade} anos")