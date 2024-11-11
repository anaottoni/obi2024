# pontuação: 100/100

k,n = input().split()

k = int(k)
n = int(n)

alfabeto = input()
mensagem = input()

aux = [False]*n

alienigena = True

for i in range(n):
    for j in range(k):
        if mensagem[i] in alfabeto:
            aux[i] = True
    
    if aux[i] == False:
        alienigena = False
        break

if alienigena == True:
    print("S")
else:
    print("N")