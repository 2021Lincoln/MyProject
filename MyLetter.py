"""É de suma importancia que seja colocado todos os nomes em inglês, tanto nas vaiaveis, quanto nos nomes dos arquivos"""

#Variaveis
nome_da_empresa = input("Digite o nome da empresa: ")
nome_do_gestor = input("Digite o nome do seu gestor: ")
cargo_atual = input("Digite seu cargo atual: ")
dada_de_inicio_aviso_previo = input("Digite a data de inicio do seu aviso previo: ")
data_do_termino_aviso_previo = input("Digite a data de termino do seu aviso previo: ")
local = input("Digite o local: ")
data = input("Digite a data: ")
assinatura = input("Digite a sua assinatura: ")
nome_completo = input("Digite seu nome completo: ")



print(f"Á {nome_da_empresa}\nPrezado(a): {nome_do_gestor},\nVenho por meio desta carta comunicar formalmente meu pedido de demissão do cargo de {cargo_atual} \nEstarei à disposição da empresa durante o aviso prévio. no periodo de {dada_de_inicio_aviso_previo} a {data_do_termino_aviso_previo}")
print(f"Local {local} e {data}")
print(f"Sua assinatura: {assinatura}")
print(f"Seu nome completo: {nome_completo}")