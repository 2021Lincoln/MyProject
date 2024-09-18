"""Um posto está vendendo combustivel com a seguinte tabela de valores:
Etanol: 3,70
Gasolina Comum: 5,39
Gasolina aditivada: 5,75
Diesel: 4,90

Escreva um programa que leia o numero de litros vendido e o tipo de combistivel(codificado da seguinte forma: 
E-etanol, GC-Gasolina comum, GA-Gasolina aditivada e D-Diesel),
Ao final de um dia mostre a qauntidade de litros e o valor arrecadado discriminado por tipo de combustivel"""


gasolina = 0
etanol = 0
gasolinaAd = 0
diesel = 0
resp = "S"
#Iniciando o bloco de repetição
while resp == "S" or resp == "s":
    #Coletando os dados
    combustivel = input("Informe o tipo de combustivel, E-etanol, GC-Gasolina comum, GA-Gasolina aditivada, D-Diesel: ")

    litros = float(input("Informe a quantidade de litros : "))
    #Acumulando as litragens por combustivel
    if combustivel == "E" or combustivel == "e":
        etanol = etanol + litros 
    elif tipo_combustivel == "GC" or combustivel "gc":
        gasolina = gasolina + litros
    elif tipo_combustivel == "GA" or combustivel == "ga":
        gasolinaAd = gasolinaAd + litros
    elif tipo_combustivel == "D" or combustivel == "d":
        diesel = diesel + litros
    else:
        print("Esse tipo de combustivel não existe")

    resp = input("Deseja continuar(S/N): ")
#Finalizando o bloco de repetição
#Apresentando os resultados
print(f"A quantidade de Etanol vendida foi: {etanol} litros, gerando um montante de R$ {(etanol * 3.70):.2f}.")
print(f"A quantidade de Gasolina comum vendida foi: {gasolina} litros, gerando um montante de R$ {(gasolina * 5.39):.2f}.")
print(f"A quantidade de Gasolina Aditivada vendida foi: {gasolinaAd} litros, gerando um montante de R$ {(gasolinaAd * 5.75):.2f}")
print(f"A quantidade de Diesel vendida foi :{diesel} litros, gerando um montante de R$ {(diesel * 4.90):.2f}.")
print(f"A quantidade total de litros vendido foi de {etanol + gasolina + gasolinaAd + diesel} litros, 
gerando um montante total de R${(etanol * 3.70) + (gasolina * 5.39) + (gasolinaAd * 5.75) + (diesel * 4.90):.2f}.")