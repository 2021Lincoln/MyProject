"""
Construa um programa que contenha uma função para transformar unidade de medida (cm p/ m ou m p/ cm).
Para isso será necessário criar uma função principal que contenha os parametros numeros e a unidade de medida
(cm ou m) e depois duas funções embutidas para transformação.
"""

#Conceito de encapsulamento
def calcular(num, unidade):     #criando a função principal
    def m(n):# criando a função metro
        return n/100
    def cm(n):# criando a função centimetro
        return n*100
    if unidade == "m":
        result = "{} centimetros.".format(cm(num))
    elif unidade == "cm":
        result = "{} metros".format(m(num))
    else:
        result = "verifique a unidade de medida."
    return result
#coletando os dados 
while True:
    try:
        n = int(input("Informe o valor da medida: "))
        u = input("Informe a unidade de medida (cm ou m): ")
    except:
        print("Verifique a entrada de dados")
    else:
        print(calcular(n,u)) #chamando a função principal
        break