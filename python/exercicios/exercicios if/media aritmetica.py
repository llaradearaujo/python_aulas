import os
os.system("cls || clear")

#solicitando dados
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite sua terceita nota :"))

#verificando
resultado = (nota1 + nota2 + nota3)/3

#exibindo dados
print("exibindo resultados: ")
print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"média: {resultado}")

if resultado >= 7:
    print("aprovado")
else:
    print("reprovado")