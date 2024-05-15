letras = []
consoantes = []
print ("Digite 10 letras, bora começar?")
for i in range(10):
    letra= input(f"Digite a {i + 1}ª letra: ")
    letras.append(letra)
    if letra.lower() not in ['a', 'e', 'i', 'o', 'u']:
        consoantes.append(letra)

print(f"As letras digitadas foram: {letras}")
print(f"As consoantes foram: {consoantes}")
        

