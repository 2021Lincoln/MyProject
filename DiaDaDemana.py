#Demonstração do uso da condicional match/case...

print("Digite o dia da semana:")
print("1. Segunda-feira")
print("2. Terça-feira")
print("3. Quarta-feira")
print("4. Quinta-feira")
print("5. Sexta-feira")
print("6. Sábado")
print("7. Domingo")

ESTADO = input("Digite a opção desejada:")


match ESTADO:
    case "Segunda-feira":
        print("Você digitou Segunda-feira")
    case "Terça-feira":
        print("Você digitou Terça-feira")
    case "Quarta-feira": 
        print("Você digitou Quarta-feira")
    case "Quinta-feira": 
        print("Você digitou Quinta-feira")
    case "Sexta-feira":
        print("Você digitou Sexta-feira")
    case "Sabado":
        print("Você digitou Sábado")
    case "Domingo":
        print("Você digitou Domingo")