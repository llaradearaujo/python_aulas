import os 
os.system("cls || clear")

soma = 0 

print("soma dos numeros impares de 1 a 9:")

for i in range(1,10):
    if i % 2 != 0:
        soma += i

print(soma)
    