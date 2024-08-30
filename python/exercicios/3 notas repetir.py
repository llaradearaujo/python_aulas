import os
os.system("cls || clear")

while True:
    nota1 = float(input("digite a primeira nota: "))
    nota2 = float(input("digite a segunda nota: "))
    nota3 = float(input("digite a terceira nota: "))
    media = (nota1+nota2+nota3)/3

    if (nota1 > 10 or nota1 < 0) or (nota2 > 10 or nota2 < 0) or (nota3 > 10 or nota3 < 0):
        print("nota inserida é maior que dez ou menor que um")
    else:
        if media >= 7: 
            print("você está aprovado!")
            break
        elif media >= 5 and media < 7:
            print("você está de recuperação!")
            break
        else:
            print("você está reprovado!")
            break