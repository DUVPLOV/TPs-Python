# Faça um programa que mostre a tabuada dos números de 1 a 10.
def Tabuada_do_um_ao_dez():
    for num1 in range (1,11):
        for num2 in range (1,11):
            print(f"{num1} * {num2} = {num1*num2}")

Tabuada_do_um_ao_dez()