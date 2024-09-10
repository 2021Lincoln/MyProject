#Demostração do uso de if/elif/else

IDADE = int(input("Digite a sua idade:"))

if IDADE < 18:
    print("Você não é maior de idade!")
    print("Não poderá realizar a operação:")
elif IDADE >= 65:
    print("Você já está pronto para se aposentar?")
    print("Poderemos oferecer suporte técnico...")
else:
    print("Você é maior de idade.")
    print("Portanto poderá realizar a operação.")

print("Obrigado por optar pelos nossos serviços!")