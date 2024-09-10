#Demonstração do uso da condicional match/case...

print("Digite o numero referente ao estado da moeda:")
print("1. Flor de cunho")
print("2. Soberba")
print("3. Muito bem conservada")
print("4. Bem conservada")
print("5. Outros estados")

ESTADO = int(input("Digite a opção desejada:"))


match ESTADO:
    case 1:
        print("Perfeita! vou pagar R$ 1.000.000.00!")
    case 2:
        print("Quase perfeita! ofereço R$ 250.000.00!")
    case 3: 
        print("Que otimo! Posso dar uns R$ 100.000.00!")
    case 4: 
        print("Quen bom. Aceitaria R$ 30.000.00!")
    case 5:
        print("Desculpe, não aceito neste estado.")
    #O ultimo case significa que qualquer coisa digitada é aceito como se fosse o else
    case _:
        print("Opção não reconhecida!")