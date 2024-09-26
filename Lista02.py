<<<<<<< HEAD
nomes = ["João", "Maria", "Pedro"]
idades = [30,25,50]

posicao = nomes.index("Maria")
print(posicao)

del nomes[posicao]
del idades[posicao]

for i in range(len(idades)):
=======
nomes = ["João", "Maria", "Pedro"]
idades = [30,25,50]

posicao = nomes.index("Maria")
print(posicao)

del nomes[posicao]
del idades[posicao]

for i in range(len(idades)):
>>>>>>> 44b534e1c634de70cf1cb94182a359216b986906
    print(nomes[i] + " " + str(idades[i]))