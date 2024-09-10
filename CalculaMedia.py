USUARIO = input("DIGITE SEU NOME: ")
NOTA_1 = float(input("Digite a sua primeira nota: "))
NOTA_2 = float(input("Digite a sua segunda nota: "))
NOTA_3 = float(input("Digite a sua terceira nota: "))

NOTA_FINAL = (NOTA_1 + NOTA_2 + NOTA_3) / 3

if NOTA_FINAL < 6:
    print(f"{USUARIO}, Aluno reprovado")
elif NOTA_FINAL >= 6:
    print(f"{USUARIO}, Aluno aprovado")
