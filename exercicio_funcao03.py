
"""Pedir 2 numeros de entrada ao usuario, perguntar qual operação matematica ele quer, criar funções para calcular as operaçoes matematica"""
#Conceito de encapsulamento
def calcular(num1, num2, op):
    try:
        def adi(x,y):
            return x+y
        def sub(x,y):
            return x-y
        def mult(x,y):
            return x*y
        def div(x,y):
            return x/y
        if op == "adi":
            result = "A soma dos numeros são: {}".format(adi(num1,num2))
        elif op == "sub":
            result = "A subtração dos numeros são: {}".format(sub(num1,num2))
        elif op == "mult":
            result = "A multiplicação dos numeros são: {}".format(mult(num1,num2))
        elif op == "div":
            result = "A divisão dos numeros são: {}".format(div(num1,num2))
        return result
    except UnboundLocalError:
        print("operador matematico invalido")
         
   
#coletando os dados 
while True:
    try:
        x = int(input("Informe um numero: "))
        y = int(input("informe outro numero: "))
        op = input("Digite qual operação matematica deseja executar, mult, adi, sub ou div: ")
    except:
        print("Verifique a entrada de dados")
    else:
        print(calcular(x,y, op)) #chamando a função principal
        break