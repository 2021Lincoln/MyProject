<<<<<<< HEAD
"""Faça um programa que leia dois vetores (Nome e nota) 
com 10 posições cada. Calcule a media das notas e informe a quantidade de 
notas abaixo e acima da media. além do nome do aluno com maior nota"""


nomes = ["Alessandra", "Maria", "Pedro", "Joao", "Otavio", "Daniele", "Gabriela", "Leandro", "Gabriel", "Lincoln", "Lucas"]
notas = [0,3,4,5,6,6,0,4,5,10,1]

maior_nota = max(notas) #Soma todas as notas
pos = notas.index(maior_nota)  #Acha a maior nota
melhor_aluno = nomes[pos] #Acha a posição da maior nota e o aluno
maior = 0
menor = 0
media = sum(notas) / len(notas) #Faz a media das notas


for i in range(len(notas)):
    if notas[i] > media:
        maior += 1
    else:
        menor += 1
print(f"A media das notas pe media {media:.2}")
print(f"A quantidade de notas acima da media foram {maior}")
print(f"A quantidade de notas abaixo da media foram {menor}")
print(f"Maior nota foi: {maior_nota}")
print(f"O melhor aluno foi: {melhor_aluno}")
=======
"""Faça um programa que leia dois vetores (Nome e nota) 
com 10 posições cada. Calcule a media das notas e informe a quantidade de 
notas abaixo e acima da media. além do nome do aluno com maior nota"""


nomes = ["Alessandra", "Maria", "Pedro", "Joao", "Otavio", "Daniele", "Gabriela", "Leandro", "Gabriel", "Lincoln", "Lucas"]
notas = [0,3,4,5,6,6,0,4,5,10,1]

maior_nota = max(notas) #Soma todas as notas
pos = notas.index(maior_nota)  #Acha a maior nota
melhor_aluno = nomes[pos] #Acha a posição da maior nota e o aluno
maior = 0
menor = 0
media = sum(notas) / len(notas) #Faz a media das notas


for i in range(len(notas)):
    if notas[i] > media:
        maior += 1
    else:
        menor += 1
print(f"A media das notas pe media {media:.2}")
print(f"A quantidade de notas acima da media foram {maior}")
print(f"A quantidade de notas abaixo da media foram {menor}")
print(f"Maior nota foi: {maior_nota}")
print(f"O melhor aluno foi: {melhor_aluno}")
>>>>>>> 44b534e1c634de70cf1cb94182a359216b986906
