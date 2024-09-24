


def soma(x, y):
        result = x + y
        print("O resultado é: ", result)
try:
    n1 = int(input("Informe um valor inteiro: "))
    n2 = int(input("Informe um valor inteiro: "))
except ValueError:
    print("verifique os valores fornecidos.")
else:
    soma(n1,n2)

