"""
Uma empresa no ramo de academias encomendou um aplicativo que fosse capaz de
armazenar alguns dados sobre os alunos, com o intuito de realizar o cálculo de IMC (Índice de
Massa Corporal). Para isso será necessário registrar em vetores o nome do aluno, o sexo, a
idade, o peso e a altura.
• IMC entre 18,5 e 24,9: peso normal;
• IMC entre 25 e 29,9: sobrepeso;
• IMC entre 30 e 34,9: obesidade grau I;
• IMC entre 35 e 39,9: obesidade grau II ou severa;
• IMC maior do que 40: obesidade grau III ou mórbida.

Ao final o aplicativo deverá listar o nome dos alunos acompanhado de seu IMC e

ainda:

• Quantidade de pessoas do sexo feminino;
• Quantidade de pessoas do sexo masculino;
• Quantidade de pessoas com Obesidade grau I, grau II e grau III;
• Quantidade de pessoas abaixo do peso;
• Percentual de pessoas do sexo feminino com Peso ideal;
• Percentual de pessoas do sexo masculino com Peso ideal;

"""

nome = []
sexo = []
idade = []
peso = []
altura = [] 

qtd_sexo_f = 0
qtd_sexo_m = 0
peso_normal = 0
sobre_peso = 0
obesidade_grau_1 = 0
obesidade_grau_2 = 0
obesidade_grau_3 = 0

resp = "S"

while resp == "S" or resp == "s":
    nome.append(input("Digite seu nome: "))
    sexo.append(input("Digite o seu sexo, M-masculino ou F-feminino:"))
    idade.append(int(input("Digite sua idade: ")))
    peso.append(float(input("Digite seu peso: ")))
    altura.append(float(input("Digite a sua altura: ")))
    resp = input("Deseja continuar (S/N)")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc >= 18.5 and imc <= 24.9:
        return "peso normal"
    elif imc >= 25 and imc <= 29.9:
        return "sobrepeso"
    elif imc >= 30 and imc <= 34.9:
        return "obesidade grau I"
    elif imc >= 35 and imc <= 39.9:
        return "obesidade grau II"
    elif imc >= 40:
        return "obesidade grau III"

# Processando dados e contando categorias
for i in range(len(nome)):
    imc_categoria = calcular_imc(peso[i], altura[i])
    
    print(f"{nome[i]} - IMC: {peso[i] / (altura[i] ** 2):.2f} ({imc_categoria})")
    
    if sexo[i] in ("F", "f"):
        qtd_sexo_f += 1
        if imc_categoria == "peso normal":
            peso_normal += 1
    elif sexo[i] in ("M", "m"):
        qtd_sexo_m += 1
        if imc_categoria == "peso normal":
            peso_normal += 1

    # Contando categorias de obesidade
    if imc_categoria == "peso normal":
        peso_normal += 1
    elif imc_categoria == "sobrepeso":
        sobre_peso += 1
    elif imc_categoria == "obesidade grau I":
        obesidade_grau_1 += 1
    elif imc_categoria == "obesidade grau II":
        obesidade_grau_2 += 1
    elif imc_categoria == "obesidade grau III":
        obesidade_grau_3 += 1

if qtd_sexo_f > 0:
    percentual_f = (peso_normal / qtd_sexo_f) * 100
    
if qtd_sexo_m > 0:
    percentual_m = (peso_normal / qtd_sexo_m) * 100

# Exibindo resultados
print("\n")
print(f"A quantidade de pessoas do sexo feminino é {qtd_sexo_f}")
print(f"A quantidade de pessoas do sexo masculino é {qtd_sexo_m}")
print(f"A quantidade de pessoas com peso normal é {peso_normal}")
print(f"A quantidade de pessoas sobre peso é {sobre_peso}")
print(f"A quantidade de pessoas com Obesidade grau I é {obesidade_grau_1}")
print(f"A quantidade de pessoas com Obesidade grau II é {obesidade_grau_2}")
print(f"A quantidade de pessoas com Obesidade grau III é {obesidade_grau_3}")
print(f"Percentual de pessoas do sexo feminino com Peso ideal: {percentual_f:.2f}%")
print(f"Percentual de pessoas do sexo masculino com Peso ideal: {percentual_m:.2f}%")