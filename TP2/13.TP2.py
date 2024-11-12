# Faça um programa que, a partir da lista:
# [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
# crie duas listas: uma com números pares e outra com números ímpares.
# Implemente uma função para determinar se um número é par ou ímpar.
# Utilize apenas os comandos ensinados em aula.
def par_ou_impar(lista):
    impares = []
    pares = []
    for num in lista:
        if(num%2==0):
            pares.append(num)
        else:
            impares.append(num)
    return{
        "pares": pares,
        "impares":impares
    }
def executar_programa():
    lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
    numeros_separados = par_ou_impar(lista)
    print(f"Pares: {numeros_separados['pares']}\nímpares: {numeros_separados['impares']}")
executar_programa()