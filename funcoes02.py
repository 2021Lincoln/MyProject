


def divide(x,y):
    try: #Aqui está sendo tratado o resultado dos dados
        result = x / y  
    except ZeroDivisionError:
        print("Verifique o denominador")
    else:
        print(f"O resultado é {result}")

try: #Aqui está sendo tratado a entrada dos dados fornecido
    n1 = int(input("Forneça um numerado: "))
    n2 = int(input("Forneça um denominador: "))
except:
    print("Verifique a entrada de dados")
else:
    divide(n1, n2)