# Faça um programa que leia um intervalo inferior e superior e mostre os números primos encontrados nesse intervalo.
# Por exemplo, para o intervalo de 5 a 10, a saída será: 5, 7.
# O programa também deve mostrar a quantidade de números primos encontrados.
# Implemente uma função para verificar se um número é primo.
from math import sqrt
def Criar_intervalo():
    print("Defina o intervalo de número que deseja descobrir quantos números primos há nele.")
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: "))
    return{
        "início":inicio,
        "fim":fim
    }
def Descobrir_numeros_primos_no_intervalo(intervalo):
    numeros_primos=[]
    qntd_primos=0
    FINAL = intervalo["fim"]
    INICIO = intervalo["início"]
    for i in range(INICIO,FINAL+1):
        if(i<1):
            continue
        div = int(sqrt(i))
        primo =True
        for testes in range(2,div+1):   
            if(i%testes==0):
                primo = False
                break

        if(primo):
            qntd_primos+=1
            numeros_primos.append(i)
    return{
        "numeros_primos":numeros_primos,
        "qntd_primos":qntd_primos
    }
intervalo = Criar_intervalo()
primos = Descobrir_numeros_primos_no_intervalo(intervalo)
print(primos["numeros_primos"], primos["qntd_primos"])
