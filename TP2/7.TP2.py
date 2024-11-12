# Faça um programa que defina a lista:
# [10, 20, 30, 40, 50, 60, 70, 80]
# e mostre seu conteúdo na ordem invertida.
# Utilize apenas os comandos ensinados em aula.

def inverter_lista(lista):
    return lista[::-1]
def executar_programa():
    lista = [10, 20, 30, 40, 50, 60, 70, 80]
    lista_invertida = inverter_lista(lista)
    print(lista_invertida)

executar_programa()