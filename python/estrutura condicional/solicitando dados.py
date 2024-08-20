import os
os.system("cls || clear") #limpa o terminal

#solicitando dados
nome = input("digite seu nome: ") #pedir ao usuario um dado do tipo texto
idade = int(input("digite sua idade: ")) #pedir dado do tipo numero inteiro
altura = float(input("digite sua altura: "))#pedir dado do tipo numero real

#exibindo dados
print(f"nome: {nome}") #f permite as chaves em torno da variavel, chaves servem para mencionar variavel
print(f"idade: {idade} anos.")
print(f"idade: {idade}; nome: {nome}")

#verificando

#TRUE = VERDADEIRO
#FALSE = FALSO
#IF = SE

if idade < 18:
    print("menoridade")

print("====fim====")