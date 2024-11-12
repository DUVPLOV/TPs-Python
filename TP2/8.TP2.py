# Faça um programa que some as seguintes listas:
# [1, 2, 3, 4, 5, 6, 7, 8]
# [10, 20, 30, 40, 50, 60, 70, 80]
# Mostre o resultado da soma em uma terceira lista.
# Exemplo:
# A soma das listas seria:
# [11, 22, 33, 44, 55, 66, 77, 88]
# Utilize apenas os comandos ensinados em aula.

def somar_listas(lista1,lista2):
    lista_final = []
    if(len(lista1)==len(lista2)):
        for i in range(len(lista1)):
            lista_final.append(lista1[i]+ lista2[i])
    return lista_final
def executar_programa():
    lista_1=[1, 2, 3, 4, 5, 6, 7, 8]
    lista_2=[10, 20, 30, 40, 50, 60, 70, 80]
    lista_somada= somar_listas(lista_1, lista_2)
    print(lista_somada)
executar_programa()