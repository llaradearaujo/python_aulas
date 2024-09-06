import os
os.system("cls || clear")

#solicitando dados
numero1 = int(input("digite numero 1 :"))
numero2 = int(input("digite numero 2 :"))

#verificar
print(f"numero um: {numero1} e numero 2: {numero2}")
if numero1 > numero2:
    print(f"maior numero: {numero1}; menor numero: {numero2}")
else:
    print(f"maior numero: {numero2} e menor numero: {numero1} ")
    
