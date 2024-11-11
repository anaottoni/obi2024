# pontuação: 40/100

def inv_col(m,n):
    if m == 2:
        for j in range(n):
            matriz[j] = [matriz[j][1], matriz[j][0]]
        return
    else:
        for j in range(n):
            aux2= matriz[j][x1]
            matriz[j][x1] = matriz[j][x2]
            matriz[j][x2] = aux2
        return
    
def imprimir ():
    if m == 2:
        for i in range(n):
            print(matriz[i][0], matriz[i][1])
        return
    else:
        for i in range(n):
            for j in range(m-1):
                print(matriz[i][j], end=" ")
            print(matriz[i][m-1])

n, m, p = input().split()

n = int(n)
m = int(m)
p = int(p)

#contador
cont = 1

#fazendo a matriz
matriz = []

if m == 2:
    for i in range(n):
        linha = []

        
        linha.append(cont)
        linha.append(cont+1)
        cont+=2

        matriz.append(linha)
else:
    for i in range(n):
        linha = []

        for j in range(m):
            linha.append(cont)
            cont+=1

        matriz.append(linha)

for i in range(p):
    passos = input().split()

    x1 = int(passos[1])-1
    x2 = int(passos[2])-1

    if passos[0] == "L":
        aux = matriz[x1]
        matriz[x1] = matriz[x2]
        matriz[x2] = aux
    else:
        inv_col(m,n)

imprimir()