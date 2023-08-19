vetor = []

ax = 1

while ax <= 5:
    dig = int(input("Digite o número: "))
    vetor.append(dig)
    ax = ax + 1
print(vetor)
print("---------------------------------------")
print(f'A soma de todos os elementos é = {sum(vetor)}')
print("---------------------------------------")
