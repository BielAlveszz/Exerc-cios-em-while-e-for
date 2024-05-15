notas = []

for i in range(4):
    nota= float(input(f"Digite a {i + 1}° nota: "))
    notas.append(nota)
    
print("Suas notas são: ")
for i, nota in enumerate(notas):
    print(f" {i + 1}° Nota: {nota}")
    
soma = sum(notas)
media = soma / len(notas)

print(f"A sua média foi: {media:.1f}")
