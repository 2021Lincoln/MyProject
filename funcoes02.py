<<<<<<< HEAD



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
=======



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
>>>>>>> 44b534e1c634de70cf1cb94182a359216b986906
    divide(n1, n2)