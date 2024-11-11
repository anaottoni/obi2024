# pontuação: 100/100

n, k = input().split()

n = int(n)
k = int(k)

notas = input().split()

for i in range(n):
    notas[i] = int(notas[i])

notas = sorted(notas)

corte = notas[n-k]

print(corte)