print("Qual sua naturalidade como torcedor")
print("Opção 1, Carioca")
print("Opção 2, Paulista")
print("Opção 3, Mineiro")

print("--"*100)
Clube_do_coracao = input("Digite a sua naturalidade como torcedor: ")

match Clube_do_coracao:
    case "Carioca":
        print("Flamengo")
        print("Botafogo")
        print("Fluminense")
        print("Vasco")
        time = (input("Qual desses times cariocas você é torcedor: "))
        if time == "Flamengo":
            print("Parabéns você é o campeão")
        elif time == "Botafogo":
            print("Parabéns, o Choro ainda não acabou")
        elif time == "Fluminense":
            print("Quase morreu na praia")
        elif time == "Vasco":
            print("Segunda divisão.................")

    case "Paulista":
        print("Gremio")
        print("Palmeiras")
        print("Santos")
        print("Corintians")
        time = (input("Qual desses times cariocas você é torcedor: "))
        if time == "Palmeiras":
            print("Parabéns você é o campeão")
        elif time == "Gremio":
            print("Parabéns, o Choro ainda não acabou")
        elif time == "Santos":
            print("Quase morreu na praia")
        elif time == "Corintians":
            print("Segunda divisão.................")
    
    case "Mineiro":
        print("Atletico-Mineiro")
        print("Internacional")
        print("Cruzeiro")
        print("Juventos")
        time = (input("Qual desses times cariocas você é torcedor: "))
        if time == "Atletico-Mineiro":
            print("Parabéns você é o campeão")
        elif time == "Internacional":
            print("Parabéns, o Choro ainda não acabou")
        elif time == "Cruzeiro":
            print("Quase morreu na praia")
        elif time == "Juventos":
            print("Segunda divisão.................")
        