"""Um posto está vendendo combustivel com a seguinte tabela de valores:
Etanol: 3,70
Gasolina Comum: 5,39
Gasolina aditivada: 5,75
Diesel: 4,90

Escreva um programa que leia o numero de litros vendido e o tipo de combistivel(codificado da seguinte forma: 
E-etanol, GC-Gasolina comum, GA-Gasolina aditivada e D-Diesel),
Ao final de um dia mostre a qauntidade de litros e o valor arrecadado discriminado por tipo de combustivel"""


resp = "S"
gasolina = 5,39
etanol = 3.70
gasolinaAd = 5.75
diesel = 4.90
soma_1 = 0
soma_2 = 0
soma_3 = 0
soma_4 = 0
while resp == "S" or resp == "s":

    tipo_combustivel = input("Informe o tipo de combustivel, E-etanol, GC-Gasolina comum, GA-Gasolina aditivada, D-Diesel: ")

    litros = float(input("Quantos litros de combustivel: "))

    if tipo_combustivel == "E":
        etanol = litros * etanol
        soma_1 += etanol 
    elif tipo_combustivel == "Gc":
        gasolina = litros * gasolina
        soma_2 += gasolina
    elif tipo_combustivel == "Ga":
        gasolinaAd = litros * gasolinaAd
        soma_3 += gasolinaAd
    elif tipo_combustivel == "D":
        diesel = litros * diesel
        soma_4 += diesel
    else:
        print("Esse tipo de combustivel não existe")

    resp = input("Deseja continuar(S/N): ")

    print(f"A quantidade de Etanol foi de: {soma_1}")
    print(f"A quantidade de Gasolina comum foi de: {soma_2}")
    print(f"A quantidade de Gasolina Aditivada foi de: {soma_3}")
    print(f"A quantidade de Diesel foi de:{soma_4}")