TIME = input("DIGITE O SEU TIME: ")
print("DIGITE A SUA POSIÇÂO NA TABELA")
print("1 para 1° lugar")
print("2 para 2° lugar")
print("3 para 3° lugar")
print("4 para 4° lugar")
print("5 para 5° lugar")
print("6 para 6° lugar")
print("7 para 7° lugar")
print("8 para 8° lugar")
print("9 para 9° lugar")
print("10 para 10° lugar")
print("11 para 11° lugar")
print("12 para 12° lugar")
print("13 para 13° lugar")
print("14 para 14° lugar")
print("15 para 15° lugar")
print("16 para 16° lugar")
print("17 para 17° lugar")
print("18 para 18° lugar")
print("19 para 19° lugar")
print("20 para 20° lugar")

POSICAO = int(input("Qual a sua posição? "))

if POSICAO == 1:
    print("CAMPEÃO")
elif POSICAO >= 1 and POSICAO <= 6:
    print("LIBERTADORES")
elif POSICAO >= 7 and POSICAO <= 12:
    print("SUL-AMERICANA")
elif POSICAO >= 13 and POSICAO <= 17:
    print("SEM CLASSIFICAÇÂO")
elif POSICAO >= 18 and POSICAO <= 20:
    print("REBAIXADO")
else: 
    print("VALOR INCORRETO! ")