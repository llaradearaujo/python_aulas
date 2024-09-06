import os
os.system("cls || clear")

contador = 0
soma:float = 0 

while True:
    print ("""
        MENU:
        S - inserir mais uma nota
        P - ver quantas notas foram inseridas
        N - calcular média aritmética das notas informadas

 """)
    opcao = input("digite uma opção: ").upper()

    match(opcao):
        case "S":
            nota = float(input("Digite uma nota: "))
            contador += 1
            soma += nota 

        case "P":
            if contador == 0:
              print("não foram inseridas notas")  
            else:
                print(f"foram inseridas {contador} notas")

        case "N": 
            media = soma/contador
            if contador == 0:
                print("não foram inseridas notas")
            else:
                print(f"Média = {media}")
                break
