import os
os.system("cls || clear")

meta_horas = int(input("digite a meta de horas de estudo: "))
soma_horas_estudadas = 0

while True:
    horas_estudadas = int(input("digite as horas estudadas: "))
    soma_horas_estudadas = soma_horas_estudadas + horas_estudadas
    
    if soma_horas_estudadas >= meta_horas:
        break

excedente = soma_horas_estudadas - meta_horas

print(f"o total de horas estudadas é de {soma_horas_estudadas} horas")
print(f"o excedente é de {excedente} horas")