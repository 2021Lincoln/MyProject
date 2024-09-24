
"""
Programa para calcular a quantidade de horas extras e exibir o resultado

"""


resp = "S"

def calc(x):
    horas = 50
    try: #Aqui está sendo tratado o resultado dos dados
        result = horas * horas_extras  
    except ValueError:
        print("Verifique o denominador")
    else:
        print(f"O valor a ser recebido de horas extras é R$ {result}")


while resp == "S" or resp == "s":       

    try: #Aqui está sendo tratado a entrada dos dados fornecido
        nome = input("Digite o nome do funcionario: ")
        horas_extras = int(input("Forneça a quantidade de horas extras: "))
    except:
        print("Verifique a entrada de dados")
    else:
        calc(horas_extras)  
        
    resp = input("Deseja continuar (S/N): ")