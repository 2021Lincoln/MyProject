#Demonstração de operadores lógicos em condicionais...
print("O que você vai fazer amanhã de manhã?")
MANHA = input("dormir / estudar / planejar: ")

print("Oque você vai fazer amanhã de tarde?")
TARDE = input("jogar / treinar / trabalhar: ")

if not MANHA or not TARDE:
    print("Você precisa dizer o que vai fazer!")
else: 
    if MANHA == "dormir" or TARDE == "jogar":
        print("Você está disperdiçando o seu dia!")
    elif MANHA == "estudar" or TARDE == "treinar":
        print("Que bom! Você irá se aperfeiçoar!")
    elif MANHA == "planejar" and TARDE == "trabalhar":
        print("Para trabalhar melhor, devo planejar!")
    else:
        print("Não combinamos estas ações...")
print("Tenha um bom dia!")