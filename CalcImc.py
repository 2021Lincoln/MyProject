USUARIO = input("DIGITE SEU NOME: ")

PESO = float(input(f"{USUARIO}, Digite o seu peso: "))
ALTURA = float(input(f"{USUARIO}, Digite a sua altura: "))

CALCFINAL = PESO/ALTURA**2

if CALCFINAL > 25:
    print("Acima do peso ideal")
elif CALCFINAL < 18:
    print("Abaixo do peso ideal")
else:
    print("Seu peso está ok!")