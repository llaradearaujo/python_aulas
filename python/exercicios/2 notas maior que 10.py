"""
escreva um algoritmo que solicite duas notas para um aluno.
caso seja menor que 0 ou maior que dez, mostre a pergunta novamente.
calcule e mostre a media aritmetica.

"""

import os
os.system("cls || clear")

while True:
    nota = float(input("digite sua primeira nota: "))
    nota2 = float(input("digite sua segunda nota:"))
    media = (nota + nota2)/2
    
    if (nota > 10 or nota < 0) or (nota2 > 10 or nota2 < 0):
        print("as notas devem ser maior que 0 e menor que 10")
        print(f"notas: {nota}, {nota2} ")
     
    else:
        print(f"media aritimetica: {media}")
        break
