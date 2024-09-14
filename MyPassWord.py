#Demostração do uso de estrutura de repetição..
CONTADOR = 0
SENHA = ""
while SENHA != "S3nh4":
    print("Digite a senha:")
    SENHA = input()

    if SENHA == "S3nh4":
        print("Senha Correta!")
        break
    else:
        print("Senha errada...")

        CONTADOR = CONTADOR + 1
        if CONTADOR == 3:
            print("Tentativas excedidas!")
            break