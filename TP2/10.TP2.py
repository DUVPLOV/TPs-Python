# Faça um programa que leia uma sequência de números, terminada pelo número zero, e armazene-os em uma lista.
# O programa deve mostrar apenas os números maiores ou iguais à média dos elementos lidos.
# Implemente uma função para ler a lista e outra para exibir os números filtrados.
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
def numeros_acima_da_media(lista):
    lista_filtrada = []
    media = sum(lista)/len(lista)
    for num in lista:
        if(num >= media):
            lista_filtrada.append(num)
    return lista_filtrada
def executar_programa():
    lista_de_numeros = criar_lista_de_numeros()
    lista_de_numeros = numeros_acima_da_media(lista_de_numeros)
    print(f"Lista filtrada: {lista_de_numeros}")
executar_programa()