# Faça um programa que leia um número do teclado e verifique se ele está presente na lista:
# [20, 10, 30, 40, 60, 50, 70, 90, 80, 100].
# Se o número for encontrado, o programa deve retornar sua posição na lista.
# Caso contrário, deve retornar -1, indicando que o número não foi encontrado.
# Implemente uma função para buscar o elemento na lista.
# Utilize apenas os comandos ensinados em aula.
def esta_presente(lista):
    num = float(input("Digite o número que deseja procurar: "))
    try:
        return lista.index(num)
    except:
        return -1
def executar_programa():
    lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]
    print(esta_presente(lista))
executar_programa()