# Faça um programa que leia uma sequência de números inteiros positivos, terminada por zero. Para cada número lido, mostre seu fatorial.
# Implemente uma função para o cálculo do fatorial.

def Criar_sequencia_de_numeros_inteiros():
    sequencia_inteiros = []
    print("Para encerrar a sequência de números inteiros, digite 0")
    num = int(input("Digite um número inteiro: "))
    while(num!=0):
        sequencia_inteiros.append(num)
        num = int(input("Digite um número inteiro: "))
    print("Sequência finalizada!")
    return sequencia_inteiros
def Existe_fatorial(numero):
    if(numero<0 or not isinstance(numero, int) ):
        print("Não existe fatorial de números decimais, números negativos ou de frações.")
        return False
    else:
        return True           
def Calcular_fatorial_de_cada_numero_da_lista(lista):
    for num in lista:
        if(num==1):
            print(f"O fatorial de {num} é 1.")
        elif(Existe_fatorial(num)):
            num_anterior = num-1
            fatorial = num
            while(num_anterior !=1):
                fatorial *=num_anterior
                num_anterior-=1
            print(f"O fatorial de {num} é {fatorial}.")

lista = Criar_sequencia_de_numeros_inteiros()
Calcular_fatorial_de_cada_numero_da_lista(lista)