Jogador1 = input("Jogador 1 digite pedra, papel o tesoura: ")
Jogador2 = input("Jogador 2 digite pedra, papel o tesoura: ")

if Jogador1 == "papel" and Jogador2 == "pedra":
    print("Jogador 1 embrulhou o jogador 2")
elif Jogador1 == "pedra" and Jogador2 == "tesoura":
    print("Jogador 1 quebrou a tesoura do jogador 2")
elif Jogador1 == "tesoura" and Jogador2 == "papel":
    print("Jogador 1 cortou o papel do jogador 2")
elif Jogador1 == Jogador2:
    print("Jogar novamente")
elif Jogador2 == "papel" and Jogador1 == "pedra":
    print("Jogador 2 embrulhou o jogador 1")
elif Jogador2 == "pedra" and Jogador1 == "tesoura":
    print("Jogador 2 quebrou a tesoura do jogador 1")
elif Jogador2 == "tesoura" and Jogador1 == "papel":
    print("Jogador 2 cortou o papel do jogador 1")
elif Jogador2 == Jogador1:
    print("Jogar novamente")