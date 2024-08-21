import os
os.system("cls || clear")

#solicitando dados
numero1= int(input("digite um número:"))
numero2= int(input("digite outro número: "))

#verificando
media = (numero1+numero2)/2
soma = numero1+numero2
produto = numero1*numero2
if numero1 > numero2:
    menorvalor = numero2
    maiorvalor = numero1
else:
      menorvalor = numero1
      maiorvalor = numero2

#exibindo dados
print(f"valores resultante: ")
print(f"média: {media}")
print(f"soma: {soma}")
print(f"produto: {produto}")
print(f"menor valor: {menorvalor}")
print(f"maior valor: {maiorvalor}")