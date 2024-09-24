"""programa feito pelo professor"""

def comb(d, c):
    try:
        litros = d / c
    except ZeroDivisionError:
        print("Verifique o consumo informado")
    else:
        print(f"A quantidade de consumo gasto foi {litros} litros")

while True:
    try:
        distancia = float(input("Informe a distancia percorrida: "))
        consumo = float(input("Informe o consumo medio do veiculo: "))
    except:
        print("Verfique os valores informado")
    else:
        comb(distancia, consumo)
        break