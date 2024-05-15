while True:
    n = int(input("Digite um número de 1 a 10: "))
    if 1  <= n <= 10:
        break
    else:
        print("Número invalido.")
        
for i in range(1, 11):
    print(str(n) + "x" + str(i) + "=" + str (n * i))
