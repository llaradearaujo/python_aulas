import os
os.system("cls || clear")

print("""
menu:
1- picanha
2- lasanha
3- strogonoff
4- bife acebolado
5- pão com ovo
      """)

prato_escolhido = int(input("qual a numeração do prato desejado? "))

match(prato_escolhido):
    case 1:
        print("prato: picanha   preço:R$35,00 ")
    case 2:
        print("prato: lasanha   preço:R$29,90 ")
    case 3:
        print("prato: strogonoff   preço:R$27,50 ")
    case 4:
        print("prato: bife acebolado   preço:R$29,50")
    case 5:
        print("prato: pão com ovo   preço:R$15,90")
    case _:
        print("opção indisponível")