import os 
os.system("cls || clear")

print("""
escolha um dia da semana:
1- domingo
2- segunda-feira
3- terça-feira
4- quarta-feira
5- quinta-feira
6- sexta-feira
7- sábado    """)

dia_escolhido = int(input("digite o número equivalente ao dia da semana para saber se ele é útil: "))

match(dia_escolhido):
    case 1:
        print("fim de semana")
    case 2:
        print("este dia é útil")
    case 3:
        print("este dia é útil")
    case 4:
        print("este dia é útil")
    case 5:
        print("este dia é útil")
    case 6:
        print("este dia é útil")
    case 7:
        print("fim de semana")
    case _:
        print("este número é inválido")

print("====FIM====")
