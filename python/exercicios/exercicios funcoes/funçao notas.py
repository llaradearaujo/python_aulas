import os
os.system("cls || clear")

def media (x,y):
    soma = x + y 
    resultado = soma/2
    return resultado

def aprovacao (a):
    if a >= 7:
        print("você está aprovado!")
    else:
        print("você está reprovado!")

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

media_final = media(nota1, nota2)
print(f"média: {media_final}")

aprovacao(media_final)