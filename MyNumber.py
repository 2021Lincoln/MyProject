#Demonstração do uso de estrutura repetitiva...
NUMERO = 1
while NUMERO >= 0:
    print("Digite um numero negativo para sair:")
    NUMERO = int(input())
    continue
    print("Este texto não será exibido! Mas... ")
else:
    print("O numero digitado foi:", NUMERO)