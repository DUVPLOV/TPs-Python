# Faça um programa que leia uma sequência de números, terminada pelo número zero, e mostre-os na ordem invertida.
# Implemente uma função para ler a lista de números e outra para exibir a lista invertida.
# Utilize apenas os comandos ensinados em aula.

def criar_lista_de_numeros():
    lista_de_numeros = []
    print("Para finalizar a sua lista/sequência de números digite 0")
    while(True):
        try:
            numero = float(input("Digite um número: "))
            break
        except:
            print("Erro: valor inválido! Digite um número!")

    while(numero!=0):
        lista_de_numeros.append(numero)
        try:
            numero = float(input("Digite um número: "))
        except:
            print("Erro: valor inválido! Digite um número!")
    lista_de_numeros.append(numero)
    print("Sequência finalizada!")
    return lista_de_numeros
def inverter_lista(lista):
    return lista[::-1]
def executar_programa():
    lista_de_nums = criar_lista_de_numeros()
    lista_invertida = inverter_lista(lista_de_nums)
    print(lista_invertida)

executar_programa()