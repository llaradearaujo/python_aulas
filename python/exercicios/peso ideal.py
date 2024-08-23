import os
os.system("cls || clear")

altura = float(input("digite sua altura: "))
sexo = input("digite a letra correspondente ao seu sexo(m:masculino ou f:feminino): ")

match sexo:
    case "m":
        pesoM = (72.7*altura)-58
        print(f"seu peso ideal é {pesoM}")
    case "f":
        pesoF = (62.1*altura)-44.7
        print(f"seu peso ideal é {pesoF}")
    case _:
        print("sexo informado é inválido")