import os
os.system("cls || clear")

def media(n1,n2):
    soma = n1 + n2
    media = soma/2
    return media

numero1 = float(input("digite a primeira nota: "))
numero2= float(input("digite a segunda nota: "))

media_aluno = media(numero1,numero2) 

print(f"a sua média é: {media_aluno}")