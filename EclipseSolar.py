LOCAL = input("DIGITE O ESTADO (RJ / SP / MG / ES): ")
print("Esteve no horario exato do eclipse?")
DIA = input("O dia está claro (S/N): ")
print("Digite a Hora para saber de você está na hora certa ou atrasado ou adiantado: ")
HORA = int(input("Se Sim, digite 0; se não, digite os minutos: "))


if DIA == "S": 
    if (LOCAL == "RJ" and HORA == 0):
        print("ASSISTINDO AO ECLIPSE TOTAL")
    elif (LOCAL == "RJ" or LOCAL == "MG" or LOCAL == "ES") and (HORA >= -5 and HORA <= 5):
        print("ECLIPSE PARCIAL")
    else:
        print("TEMPO RUIM PARA ASSISTIR")
    