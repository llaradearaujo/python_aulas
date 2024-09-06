import os 
os.system("cls || clear")

def soma(n1, n2):
    soma = n1+n2
    return soma

def  multiplicacao (n1,n2):
    multiplicacao = n1*n2
    return multiplicacao

def subtraçao (n1,n2):
    subtraçao = n1 - n2
    return subtraçao

def divisao (n1,n2):
    divisao = n1/n2
    return divisao

numero1 = float(input("digite um número: "))
numero2 = float(input("digite outro número: "))

divisao_resultado = divisao(numero1,numero2)
soma_resultado = soma(numero1, numero2)
multiplicacao_resultado = multiplicacao(numero1, numero2)
subtracao_resultado = subtraçao(numero1, numero2)

print(f"o resultado da divisão é: {divisao_resultado}")
print(f"o resultado da soma é: {soma_resultado}")
print(f"o resultado da subtração é: {subtracao_resultado}")
print(f"o resultado da multiplicação é: {multiplicacao_resultado}")