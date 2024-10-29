# Crie um programa que peça ao usuário para inserir dois números e, em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números
def todas_as_operacoes(num1,num2):
    print(f"O resultado da soma dos números é {num1+num2}")
    print(f"O resultado da subtração dos números é {num1-num2}")
    print(f"O resultado da multiplicação dos números é {num1*num2}")
    if(num2 ==0):
        print("Não é possível realizar divisão por zero")
    else:
        print(f"O resultado da divisão dos números é {num1/num2}")
        print(f"O resultado da divisão inteira dos números é {num1 //num2}")

num1 = float(input("Insira um número: "))
num2 = float(input("Insira outro número: "))

todas_as_operacoes(num1,num2)

