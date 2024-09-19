"""Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões,
sabendo que serão fornecidos pelo usuario as letras assinaladas em cada questão. Para isso será 
criado um vetor chamado GABARITO com as seguintes respostas: A, B, B, D, E"""


gabarito = ["A", "B", "B", "D", "E"]
resultado = [0]

for i in range(gabarito):
    letra = input("Digite a letra desejada: ")
    if letra[i] == resultado[0]:
        resultado.append()
