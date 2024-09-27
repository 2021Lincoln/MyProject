
resp = "S"
idade = []
sexo = []
qtd_curso = []
qtd_m = 0
qtd_zero = 0
qtd_dois = 0
qtd_tres_cinco = 0
qtd_cinco = 0
qtd_f = 0
qtd_maior18 = 0
qtdmenor_18 = 0
while resp == "S" or resp == "s":
    idade.append(int(input("Informe a idade: ")))
    sexo.append(input("Informe o seu sexo M - masculino ou F - Feminino"))
    qtd_curso.append(int(input("Informe a quantidade de cursos realizados: ")))
    resp = input("Deseja continuar(S/N)? ")
for i in range(len(idade)):
    if qtd_curso[i] == 0:
        qtd_zero += 1
    elif qtd_curso[i] >= 1 and qtd_curso[i] <= 2:
        qtd_dois += 1
    elif qtd_curso[i] >= 3 and qtd_curso[i] <= 5:
        qtd_tres_cinco += 1
    elif qtd_curso[i] > 5:
        qtd_cinco += 1
    #Desvio condicional para sexo
    if sexo[i] == "M" or sexo[i] == "m":
        qtd_m += 1
    elif sexo[i] == "F" or sexo[i] == "f":
        qtd_f += 1 

    #Desvio condicional para idade
    if idade[i] >= 18:
        qtd_maior18 += 1
    else:
        qtdmenor_18 += 1
print(f"A quantidade de estudante que não realizaram cursos é {qtd_zero} compreendendo o percentual de {(qtd_zero/len(idade))*100:.0f} %")
print(f"A quantidade de estudade que realizaram entre 1 e 2 cursos são {qtd_dois}, compreendendo o percentual de {(qtd_dois/len(idade))*100:.0f} % ")
print(f"A quantidade de estudante que realizaram entre 3 a 5 cursos são {qtd_tres_cinco}, compreendendo o percentual de {(qtd_tres_cinco/len(idade))*100:.0f} %")
print(f"A quantidade de estudande maiores de idade são {qtd_maior18} e a quantidade menores de idade são {qtdmenor_18}")
print(f"A quantidade de estudante do sexo masculino são {qtd_m} e a quantidade do sexo feminino são {qtd_f}")

print(f"A quantidade de estudante que participaram da pesquisa são {len(idade)}")