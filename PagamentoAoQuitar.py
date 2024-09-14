Valor_produto = float(input("Insira o valor do produto: "))

Taxa_juros = float(input("Insira a taxa de juros: "))

Qtd_parcela = int(input("Insira a quantidade de parcelas: "))

pagar = Valor_produto/Qtd_parcela

Acumulado = 0
x = ""
while x != "Interromper":
    for x in range(0, Qtd_parcela):
        print(f"Deseja pagar a {x+1} parcela?")
        pagar = input()
        if pagar == "sim":
            Qtd_parcela = Qtd_parcela * (1 + Taxa_juros)
            Acumulado = Acumulado + Qtd_parcela
else:
    print("Sair do programa")

"""
TERMINAR EM CASA, POIS Ñ CONSEGUI TERMINAR

"""