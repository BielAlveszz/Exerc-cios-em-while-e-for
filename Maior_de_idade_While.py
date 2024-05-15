idade_maior = 0
i = 0
while i < 5:
      old = int(input("Digite a idade da pessoa: "))
      if old > 18:
          idade_maior += 1
      i += 1
print("Número de pessoas maiores de idade:", idade_maior)
