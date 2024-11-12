# Faça um programa que mostre o menor, o maior, a soma e a média dos elementos da lista:
# [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
# Utilize apenas os comandos ensinados em aula.
def encontrar_maior_menor_e_media(lista):
    menor = min(lista)
    maior = max(lista)
    media = sum(lista) / len(lista)
    return{
        "maior":maior,
        "menor":menor,
        "média":media
    }
def executar_programa():
    lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
    resultado_filtro = encontrar_maior_menor_e_media(lista)
    print(f"Maior: {resultado_filtro["maior"]}\nMenor: {resultado_filtro["menor"]}\nMédia: {resultado_filtro["média"]}")
executar_programa()