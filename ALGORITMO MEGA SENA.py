n = []
c = 0

while c < 6:
    numero = int(input("Digite um número (positivo e menor ou igual a 60): "))
    
    if numero > 0 and numero <= 60 and numero not in n:
        n.append(numero)
        c += 1
    else:
        print("Você não pode escolher o mesmo número já escolhido.")
        
print("Números escolhidos: ", n)
