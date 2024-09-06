import os
os.system("cls || clear")

#função sem retorno
def logo_senai(): #def = palavra que indica a construção de uma função
    os.system("cls || clear")
    print(""" 
===============
    senai
===============          
""")
    
logo_senai() #quando se cita uma função tudo que está dentro dela será executado
nome = input("digite seu nome: ")

logo_senai()
idade = input("digite sua idade: ")

logo_senai()
nota = input("digite sua nota: ")

os.system("cls || clear")

#função com retorno - return
def somar(n1:int, n2:int):
    soma = n1 + n2
    return soma 

numero_1 = int(input("digite um número: "))
numero_2 = int(input("digite outro número: "))

soma = somar(numero_1, numero_2)


print(f"soma: {soma}")