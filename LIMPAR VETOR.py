vetor = []

ax = 1

while ax <= 10:
    dig = int(input("Digite o número: "))
    vetor.append(dig)
    ax = ax + 1

v = [ele for ele in vetor if ele > 0]

print(v)
