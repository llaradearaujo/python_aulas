import os
os.system("cls || clear")

def imc_calculo(altura, peso):
    imc = peso/(altura*altura)
    return imc

def imc_classificacao(imc):

    if imc < 18.5:
        print("abaixo do peso")
        print("consulte um nutricionista!")
    elif imc > 18.5 and imc < 25:
        print("peso normal")
        print("mantenha hábitos saudáveis!")
    elif imc >= 25 and imc < 30:
        print("sobrepeso")
        print("considere uma dieta e atividade física!")
        print("obesidade grau 1")
        print("procure um profissional de saúde!")
    elif imc >= 35 and imc < 40:
        print("obesidade nível 2")
        print("consulte um médico para avaliação!")
    else:
        print("obesidade nível 3")
        print("busque assistência médica imediatamente!")

altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))

imc = imc_calculo(altura, peso)
print(f"seu imc (indíce de massa corporal) é de: {imc:.2f}")

classificaçao = imc_classificacao(imc)

