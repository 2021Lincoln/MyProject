SERVICOS = input("Os serviços foram prestados? (S/N) ")
if SERVICOS == "S":
    NOTA = int(input("Digite a nota para os serviços prestados: "))


if SERVICOS == "S":
    if NOTA == 1:
        print("Pessimo")
    elif NOTA == 2:
        print("Ruim")
    elif NOTA == 3: 
        print("Razoavel")
    elif NOTA == 4:
        print("Bom")
    elif NOTA == 5:
        print("Otimo")
elif SERVICOS == "N":
    print("Serviços não foram prestados!")
    RECLAMACAO = input("Deseja efetuar uma reclamação? (S/N)")
    if RECLAMACAO == "S":
        RECLAMACAO_RECEBIDA = input("Escreva a sua reclamação: ")
        print(RECLAMACAO_RECEBIDA)
        print("Reclamação registrada, desculpe pelo trantorno!")
    else:
        print("Desculpe pelo transtorno")