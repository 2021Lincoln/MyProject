
#Append() adiciona um elemento na lista
#insert() Aqui insert
#remove() remove o objeto de dentro da lista em especifico exemplo Lista.remove("BLOG")
#pop() 
#del() Remove a posição da lista exemplo Lista.del(2) aqui está removendo na posição 2
#clear() Limpa toda a lista exemplo Lista.clear()
#sort() ordena os numeros
#index() encontra a posição de um valor especifico

#Declarando as Listas
nomes = ["João", "Maria", "Pedro"]
idades = [30,25,50]

#Exibindo o conteudo das Listas
print(nomes[0])
print(idades[0])

nomes.append("Joana")
idades.append(45)
#Exibindo todo o conteudo das listas com repetição
for i in range(len(idades)):
    print(nomes[i])
    print(idades[i])
    nomes.append(input("Informe o nome: "))
    idades.append(int(input("Informe a idade: ")))

#Exibindo todo o conteudo das listas com repetição
for i in range(len(idades)):

     print(f"Sr(a) {nomes[i]}, a sua idade é {idades[i]} anos.")
