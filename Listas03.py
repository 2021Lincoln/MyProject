#len() conta todo o tamanho do vetor
#sum() soma todos os valores das posições do vetor


#Declarando as variaveis
notas = []
resp = "S"
cont_notas = 0
soma_notas = 0
#Iniciando o bloco de repetição
while resp == "S" or resp == "s":
    #Alimentando a lista
    notas.append(float(input("Informe as notas: ")))
    resp = input("Deseja continuar (S/N)? ")
#Finalizando o bloco de repetição
    
#Iniciado o bloco de repetição
for i in range(len(notas)):
    print(notas[i])#Exibindo o conteudo da lista
    soma_notas += sum(notas) #Somando as notas
#Finalizando o bloco de repetição
print("A media foi ", soma_notas / len(notas)) 
