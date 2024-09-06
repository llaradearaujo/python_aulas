import os 
os.system("cls || clear")

total_calorias = 2000
soma_calorias = 0

while  soma_calorias < total_calorias:
    calorias_consumidas = int(input("digite as calorias consumidas: "))
    soma_calorias = soma_calorias + calorias_consumidas

    

excedente = soma_calorias - total_calorias

print(f"o total consumido foi de {soma_calorias} calorias")
print(f"o excedente calórico foi de {excedente} calorias")


#if soma_calorias > total_calorias:
       # break