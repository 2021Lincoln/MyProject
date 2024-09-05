#Declaração de variaveis...
MyName = "Lincoln Oliveira"
MyHeigth = 1.79
MyAge = 32
TimeDoCoracao = "Flamengo"
Animais_domesticos = 0
Contato = 21960154311
Cor_dos_olhos = "mel"



#Exibição do conteudo das variaveis....
# print("Meu nome é ", MyName, ".")
# print("Minha altura é de ", MyHeigth, "metros")
# print("Minha idade é: ", MyAge, "anos")
# print("Time do coração: ", TimeDoCoracao)
# print("Cor dos olhos: ", Cor_dos_olhos)
# print("contato: ", Contato)
# print("Quantidade de animais domesticos: ", Animais_domesticos)


print("------------------------------------------------------------------------")

print("Dados do Usuario")

print("\nDigite seu nome: ")
MyName = str(input())

print("\nDigite a sua altura: ")
MyHeigth = float(input())

print("\nDigite a sua idade: ")
MyAge = int(input())

print("\nDigite a cor dos olhos: ")
Cor_dos_olhos = str(input())

print("\nDigite seu numero de contato: ")
Contato = int(input())

print("\nDigite quantos animais você tem? ")
Animais_domesticos = int(input())

print("------------------------------------------------------------------------")

print("\nMeu nome é", MyName, ".")
print("Minha altura é de", MyHeigth, "metros")
print("Minha idade é:", MyAge, "anos")
print("A cor dos seus olhos é", Cor_dos_olhos)
print("Seu numero de contato é ", Contato)
print("Você tem:", Animais_domesticos, "animais domesticos")