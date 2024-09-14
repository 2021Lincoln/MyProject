
Resposta = ""

while Resposta != "Flamengo":
    print("Qual o melhor clube de futebol do Brasil: ")
    Resposta = input()
    if Resposta != "Flamengo":
        print("Você está sendo advertido, pois digitou o time errado")
    continue
else:
    print("Resposta Correta, O melhor time é o Mengão....")