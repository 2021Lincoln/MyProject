"""
A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. 
Faça um programa para coletar dados sobre a renda familiare numero de filhos de cada habitantate e ao final, mostre:

a) Média de salario da população
b) Média de numeros de filhos
c) Maior salario dos habitantes 
d) percentual de pessoas com salario menor que R$1500,00.

"""
soma_renda = 0
soma_qtd_filhos = 0
maior_renda = 0
qtd_renda = 0

for cont in range(3):
    #Coletando os dados
    renda = float(input("Digite a renda familiar: "))
    qtd_filhos = int(input("Digite o numero de filhos: "))
    #Acumulando os dados
    soma_renda += + renda
    soma_qtd_filhos += qtd_filhos
    #Coletando a maior renda
    if renda > maior_renda:
        maior_renda = renda
    #Coletando renda menor que 1500
    if renda < 1500:
        qtd_renda += 1
    
#Final do bloco de repetição
print(f"A media das rendas: {soma_renda/cont}")
print(f"A media das quantidade de filhos: {soma_qtd_filhos/cont}")
print(f"A Maior renda é: {maior_renda}")
print(f"O percentual de pessoas com renda abaixo de 1500 é: {(qtd_renda/cont)*100}")