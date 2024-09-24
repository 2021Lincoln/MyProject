"""Construa um programa que informe ao usuario atraves de uma função a quantidade de litros de combustivel
gasto em uma viagem. será necessário informar a distancia percorrida e o consumo médio do veiculo"""

percurso = 400

def qtd_litros(a,b):
    try:
        qtd = a / b
    except ZeroDivisionError:
        print("Verifique o consumo informado")  
    else: 
        print(f"A quantidade de consumo gasto foi {qtd} litros")
while True:
    litros = float(input("Informe a quantidade de litros de combustivel gasto? "))
    if litros == "":
        print("Deve informar a quantidade de litros gastos")
    break

if litros != "":
    try:
        while True:
            distancia = float(input("Informe a distancia percorrida: "))
            if distancia == "":
                print("Você não informou os dados corretamente!!!!")
            break
    except:
        print("Verfique os valores informado")

else:
    print("Você não informou os dados corretamente!!!!")

print(f"Você percorreu {distancia} quilometros")
qtd_litros(litros, distancia)

