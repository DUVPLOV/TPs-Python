# Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).
# O IMC é calculado dividindo o peso (em kg) pelo quadrado da altura (em metros).
# resultados menores que 16 — magreza grave;
# resultados entre 16 e 16,9 — magreza moderada;
# resultados entre 17 e 18,5 — magreza leve;
# resultados entre 18,6 e 24,9 — peso ideal;
# resultados entre 25 e 29,9 — sobrepeso;
# resultados entre 30 e 34,9 — obesidade grau I;
# resultados entre 35 e 39,9 — obesidade grau II ou severa;
# resultados maiores do que 40 — obesidade grau III ou mórbida.

def calcular_imc(peso,altura):
    imc = peso / (altura ** 2)
    if(imc<16):
        print("Você está com magreza grave!")
    elif(imc<=16.9):
        print("Você está com magreza moderada")
    elif(imc <=18.5):
        print("Você está com magreza leve")
    elif(imc<=24.9):
        print("Você está com o peso ideal")
    elif(imc<=29.9):
        print("Você está com sobrepeso")
    elif(imc<=34.9):
        print("obesidade grau I;")
    elif(imc<=39.9):
        print("obesidade grau II ou severa")
    elif(imc>40):
        print("Você está obesidade grau III ou mórbida!")
    print(f"Resultado: {imc:.2f}")

kg = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite o sua altura em metros: "))

calcular_imc(kg,altura)