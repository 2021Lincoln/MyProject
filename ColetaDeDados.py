"""
Foi realizada um pesquisa de algumas caracteristica fisica da população de um certa região, a qual coletaram
os seguintes dados referentes a cada  habitante para serem analisados:
sexo(masculino e feminino)
cor dos olhos(azuis, verde ou castanhos)
cor dos cabelos(louros, castanhos, preto)
idade
Faça um programa que determine e escreva:
a) A maior idade dos habitantes:
b) A quantidade de individuos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive:
c) A quantidade de individuos que tenha olhos verdes e cabelos louros:
"""


sexo = []
cor_dos_olhos = []
cor_dos_cabelos = []
idade = []
sexo_feminino = ""
olhos = ""
cabelos = ""
resp = "S"
cont = 0
cont = 0
qtd_olhos_cabelos = 0
qtd_sexo_f = 0

while resp == "S" or resp == "s":
    idade.append(int(input("Digite a sua idade: ")))
    sexo.append(input("Digite o seu sexo masculino ou feminino: "))
    cor_dos_olhos.append(input("Digite a cor dos olhos, azuis, verde ou castanhos: "))
    cor_dos_cabelos.append(input("Digite a cor dos seus cabelos, louros, castanhos, preto: "))

    maior_idade = max(idade)
    pos = idade.index(maior_idade)
    for i in range(len(idade)):
        if (sexo[i] == "F" or sexo[i] == "f") and (idade[i] >= 18 and idade[i] <= 35):
            qtd_sexo_f += 1
        if (cor_dos_olhos[i] == "V" or cor_dos_olhos[i] == "v") and (cor_dos_cabelos[i] == "L" or cor_dos_cabelos[i] == "l"):
            qtd_olhos_cabelos += 1
    resp = input("Digite (S)Sair / tecle qualquer letra != de S para continuar: ")
print(f"A maior idade dos habitantes é de: {maior_idade}")
print(f"A quantidade de individuo do sexo feminino cuja idade entre 18 e 35 anos é: {qtd_sexo_f}")
print(f"A quantidade de individuos que tenham olhos verdes e cabelos louros é: {qtd_olhos_cabelos}")