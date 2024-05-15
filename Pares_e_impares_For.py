numeros = []
numerosX = []
numerosB = []

print("Digite 10 números inteiros, vamos começar?")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}° número: "))
    numeros.append(numero)
    if numero % 2 == 0: #
       numerosX.append(numero)
    else:
        numerosB.append(numero)

print(f"Os números digitados foram: {numeros}")
print(f"Os números pares foram: {numerosB}")
print(f"Os números ímpares foram: {numerosX}")
