"""
Escreva um programa que armazene o nome de 10 pessoas em um vetor. Após isto o programa deve solicitar um nome qualquer
e em seguida escrever a mensagem USUARIO ENCONTRADO, se o nome estiver entre os 10 nomes armazenados, ou USUARIO NÂO ENCONTRADO.
"""



nomes = ["Joana", "Maria", "Rafaela", "Ricardo", "Juan", "Ana", "Gustavo", "Guilherme", "Allan", "Daniele"]

pesquisa = (input("Informe um nome a ser procurado: "))
for i in range(len(nomes)):
    if nomes[i] == pesquisa:
        resp = "Usuario encontrado"
        break
    else:
        resp = "Usuario não encontrado"
print(resp)








