nomes = ["João", "Maria", "Pedro"]
idades = [30,25,50]

posicao = nomes.index("Maria")
print(posicao)

del nomes[posicao]
del idades[posicao]

for i in range(len(idades)):
    print(nomes[i] + " " + str(idades[i]))