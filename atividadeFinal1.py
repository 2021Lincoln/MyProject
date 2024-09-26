"""
Uma empresa na area do varejo encomendou uma pesquisa para saber a opnião das pessoas em relação ao gosto de um determinado produto no mercado.
Para isso será necessário armazenar em vetores as seguintes informações:
O sexo do entrevistado (M ou F):
A sua idade:
E a resposta sobre o produto (S ou N).

Sabendo-se que foram entrevistadas um numero x de pessoas, elabore um programa que informe:

O total de pessoas que participaram da pesquisa:
O numero de pessoas que responderam SIM:
O numero de pessoas que responderam NÂO:
Quantas pessoas maiores de 18 anos gostaram do produto:
Quantas pessoas menores de 18 anos não gostaram do produto:
Quantas pessoas maiores de 18 anos do sexo feminino. não gostaram do produto?
Quantas pessosas menores de 18 anos, do sexo masculino, gostaram do produto.

"""

resp = "S"
idade = []
sexo = []
produto = []
qtd_maior18 = 0
qtd_menor_18 = 0
qtd_f = 0
qtd_m = 0
total = 0
qtd_sim = 0
qtd_nao = 0

while resp == "S" or resp == "s":
    idade.append(int(input("Informe a idade: ")))
    sexo.append(input("Informe o seu sexo M - masculino ou F - Feminino: "))
    produto.append(input("Gostou do produto (S-sim/N-não): "))
    resp = input("Deseja continuar(S/N)? ")
for i in range(len(idade)):
    if idade[i]:
        total += 1
    elif produto[i] == "S" or produto[i] == "s":
        qtd_sim += 1
    elif produto[i] == "N" or produto[i] == "n":
        qtd_nao += 1
    elif produto[i] == "S" or produto[i] == "s" and idade > 18:
        qtd_maior18 += 1
    elif produto[i] == "N" or produto[i] == "n" and idade < 18:
        qtd_menor_18 += 1
    elif produto[i] == "N" or produto[i] == "n" and sexo[i] == "F" or sexo[i] == "f" and qtd_maior18:
        qtd_f += 1
    elif produto[i] == "S" or produto[i] == "s" and sexo[i] == "M" or sexo[i] == "m" and qtd_menor_18:
        qtd_m += 1
    #Desvio condicional para sexo
    if sexo[i] == "M" or sexo[i] == "m":
        qtd_m += 1
    elif sexo[i] == "F" or sexo[i] == "f":
        qtd_f += 1 

    #Desvio condicional para idade
    if idade[i] >= 18:
        qtd_maior18 += 1
    else:
        qtd_menor_18 += 1
print(f"O total de pessoas que participaram da pesquisa: {total}")
print(f"O numero de pessoas que responderam SIM: {qtd_sim}")
print(f"O numero de pessoas que responderam NÂO: {qtd_nao}")
print(f"Quantas pessoas maiores de 18 anos gostaram do produto: {qtd_maior18}")
print(f"Quantas pessoas maiores de 18 anos do sexo feminino. não gostaram do produto: {qtd_f}")
print(f"Quantas pessosas menores de 18 anos, do sexo masculino, gostaram do produto: {qtd_m}")




###Terminar em casa 