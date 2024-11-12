# Desenvolva um programa que peça ao usuário para escolher uma operação (adição, subtração, multiplicação, divisão) e dois números, e então execute a operação escolhida com os números

print("Escolha uma operação: adição (+), subtração (-), multiplicação (*) ou divisão (/)\nUtilize os simbolos correspondentes a operação para escolhê-la.")

def realizar_operacao(num1,num2,op):
    match op:
        case "+":
            print(f"O resultado da soma de {num1} e {num2} é {num1+num2}")
        case "-":
                print(f"O resultado da subtração de {num1} e {num2} é {num1-num2}")

        case "*":
                print(f"O resultado da multiplicação de {num1} e {num2} é {num1*num2}")

        case "/":
                if num2 != 0:
                    print(f"O resultado da divisão de {num1} e {num2} é {num1/num2}")
                else: 
                    print("Não é possível dividir por zero.")

        case _:
            print("Operação inválida!")

op = input("Digite a operação: ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
realizar_operacao(num1,num2,op)