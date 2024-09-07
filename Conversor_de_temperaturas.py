#Converter de celsius para kelvin e farenheit
celsius = float(input("Digite a temperatura em CELSIUS: "))
fahrenheit = 32 + (9/5 * celsius)
kelvin = celsius + 273

print(f"A temperatura de celsius é: {celsius} °C")
print(f"A temperatura de fahrenheit é: {fahrenheit} °F")
print(f"A temperatura de kelvin é: {kelvin} K")



print("-"*100)

#Converter de kelvin para celsius e farenheit
kelvin = float(input("Digite a temperatura em kelvin: "))
celsius = kelvin - 273.15
fahrenheit = (kelvin - 273.15) * 9/5 + 32 

print(f"A temperatura de celsius é: {celsius} °C")
print(f"A temperatura de fahrenheit é: {fahrenheit} °F")
print(f"A temperatura de kelvin é: {kelvin} K")



print("-"*100)

#Converter de farenheit para celsius e kelvin
fahrenheit = float(input("Digite a temperatura em fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
kelvin = (fahrenheit - 32) * 5/9 + 273.15
print(f"A temperatura de celsius é: {celsius} °C")
print(f"A temperatura de fahrenheit é: {fahrenheit} °F")
print(f"A temperatura de kelvin é: {kelvin} K")