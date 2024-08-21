import os
os.system("cls || clear") 

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

print("""
+: soma
-: subtração
*: multiplicação
/: divisão
""")

opcao = input("digite uma opção: ")
match(opcao):
    case "+":
        resultado = numero1+numero2
    case "-":
        resultado = numero1-numero2
    case"*":
        resultado = numero1*numero2
    case"/":
        resultado = numero1/numero2
    case _:
        print("opção inválida")

print(f"resultado: {resultado}")
