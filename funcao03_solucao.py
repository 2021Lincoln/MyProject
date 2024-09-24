"""
Programa para calcular a quantidade de horas extras e exibir o resultado

"""


### Criando a função calculo
def calculo(valor):
    result = valor * 50
    print(f" Sr {nome}, irá receber o valor de R$ {result:.2f}")
#Iniciando um loop infinito
while True: 
    nome = input("Informe o nome do funcionario: ")
    if nome != "":
        break #Finalizando o loop infinito
    else:
        print("Verifique o nome fornecido")
        
#Iniciando um loop infinito
while True:
    try:
        horas_extras = float(input("Informe a quantidade de horas trabalhadas: "))
    except ValueError:
        print("Verifique a quantidade de horas extras")
    else:
        calculo(horas_extras)
        break #Finalizando o loop infinito

