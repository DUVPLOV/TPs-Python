# Neste exercício, você deverá escrever um programa em Python que verifique se um número fornecido pelo usuário é par ou ímpar. Imprima uma mensagem indicando se o número é par ou ímpar.

def par_ou_impar(numero_user):
    if (numero_user%2==0):
        print(f"O número {numero_user} é par.")
    else:
        print(f"O número {numero_user} é ímpar.")

numero = int(input("Digite o número que deseja verificar se é par ou ímpar: "))
par_ou_impar(numero)