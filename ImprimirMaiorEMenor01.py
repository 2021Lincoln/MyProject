num = [30,25,50,10,15,25,40,90,85,20]
maior = num[0]
menor = num[0]

for i in range(len(num)):
    if num[i] > maior:
        maior = num[i]
    if num[i] < menor:
        menor = num[i]

print("O maior valor é: ", maior)
print("O menor valor é: ", menor)


