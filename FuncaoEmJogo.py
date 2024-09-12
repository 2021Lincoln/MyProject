print("Funções em um jogo de futebol, goleiro, zagueiro, lateral, ala, volante, meia, meio-campo, atacante ou centravante")
POSICAO = input("DIGITE A SUA FUNÇÂO EM UM JOGO: ")

if POSICAO == "goleiro" or POSICAO == " zagueiro" or POSICAO == "lateral":
    print("DEFESA")
elif POSICAO == "ala" or POSICAO == "volante" or POSICAO == "meia":
    print("MEIO-CAMPO")
elif POSICAO == "ponta" or POSICAO == "atacante" or POSICAO == "centravante":
    print("ATAQUE")
else:
    print("Você deve ser teimoso...")