print("DIGITE 3 NUMEROS DISTINTOS: ")
X = int(input("DIGITE O PRIMEIRO NUMERO: "))
Y = int(input("DIGITE O SEGUNDO NUMERO: "))
Z = int(input("DIGITE O SEGUNDO NUMERO: "))

if X > Y and X > Z:
    print("OS NUMEROS ESTÂO EM ORDEM DECRESCENTE")
elif X < Y and Y < Z:
    print("ESTÁ EM ORDEM CRESCENTE:")
else:
    print("ELES ESTÂO MISTURADOS")